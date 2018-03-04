import json
import pytest

from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from mixer.backend.django import mixer

from comments.models import Comment
from posts.models import Post


User = get_user_model()


@mixer.middleware(User)
def encrypt_password(user):
    user.set_password('test')
    return user


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_list_posts(client):

    mixer.cycle(5).blend(Post)

    response = client.get('/api/posts/')
    assert response.status_code == 200

    data = json.loads(response.content)
    assert data['count'] == 5


@pytest.mark.django_db
def test_create_post(client):

    user = mixer.blend(User)
    client.login(username=user, password='test')

    data = {
        'title': 'testing...',
        'url': 'https://space.com',
    }

    response = client.post('/api/posts/', data, format='json')
    assert response.status_code == 201

    post = Post.objects.first()
    assert post.title == 'testing...'
    assert post.url == 'https://space.com'
    assert post.author == user


@pytest.mark.django_db
def test_retrieve_post(client):

    post = mixer.blend(Post)
    response = client.get(f'/api/posts/{post.id}/')
    assert response.status_code == 200

    data = json.loads(response.content)
    assert data['title'] == post.title
    assert data['author']['username'] == post.author.username


@pytest.mark.django_db
def test_comments(client):

    post = mixer.blend(Post)
    mixer.cycle(5).blend(Comment, post=post)
    response = client.get(f'/api/posts/{post.id}/comments/')
    assert response.status_code == 200

    data = json.loads(response.content)
    assert len(data) == 5


@pytest.mark.django_db
def test_add_comment(client):

    post = mixer.blend(Post)
    user = mixer.blend(User)

    client.login(username=user.username, password='test')

    data = {'content': 'testing'}

    response = client.post(
        f'/api/posts/{post.id}/add_comment/',
        data,
        format='json',
    )
    assert response.status_code == 201

    comment = Comment.objects.first()
    assert comment.author == user
    assert comment.post == post
    assert comment.content == 'testing'


@pytest.mark.django_db
def test_update_post(client):

    post = mixer.blend(Post)

    data = {
        'title': 'testing...',
        'url': 'https://space.com',
    }

    client.login(username=post.author.username, password='test')

    response = client.put(f'/api/posts/{post.id}/', data, format='json')
    assert response.status_code == 200

    post.refresh_from_db()

    assert post.title == 'testing...'
    assert post.url == 'https://space.com'


@pytest.mark.django_db
def test_delete_post(client):

    post = mixer.blend(Post)

    client.login(username=post.author.username, password='test')
    response = client.delete(f'/api/posts/{post.id}/')

    assert response.status_code == 204
    assert not Post.objects.exists()
