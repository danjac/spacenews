import pytest

from unittest import mock

from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

from mixer.backend.django import mixer

from posts.models import Post
from posts.permissions import PostPermission

User = get_user_model()


@pytest.fixture
def req():
    return HttpRequest()


def test_get_all_if_anonymous(req):

    req.method = 'GET'
    req.user = AnonymousUser()

    perm = PostPermission()
    assert perm.has_permission(req, mock.Mock())


def test_get_all_if_authenticated(req):

    req.method = 'GET'
    req.user = User()

    perm = PostPermission()
    assert perm.has_permission(req, mock.Mock())


def test_post_if_anonymous(req):

    req.method = 'POST'
    req.user = AnonymousUser()

    perm = PostPermission()
    assert not perm.has_permission(req, mock.Mock())


def test_post_if_authenticated(req):

    req.method = 'POST'
    req.user = User()

    perm = PostPermission()
    assert perm.has_permission(req, mock.Mock())


def test_get_instance_if_anonymous(req):

    req.method = 'GET'
    req.user = AnonymousUser()

    perm = PostPermission()
    assert perm.has_object_permission(req, mock.Mock(), Post())


def test_get_instance_if_authenticated(req):

    req.method = 'GET'
    req.user = User()

    perm = PostPermission()
    assert perm.has_object_permission(req, mock.Mock(), Post())


def test_put_instance_if_anonymous(req):

    req.method = 'PUT'
    req.user = AnonymousUser()

    perm = PostPermission()
    assert not perm.has_object_permission(req, mock.Mock(), Post())


@pytest.mark.django_db
def test_put_instance_if_authenticated_not_author(req):

    req.method = 'PUT'
    req.user = User()

    post = mixer.blend(Post)

    perm = PostPermission()
    assert not perm.has_object_permission(req, mock.Mock(), post)


@pytest.mark.django_db
def test_put_instance_if_authenticated_is_author(req):

    post = mixer.blend(Post)

    req.method = 'PUT'
    req.user = post.author

    perm = PostPermission()
    assert perm.has_object_permission(req, mock.Mock(), post)


def test_delete_instance_if_anonymous(req):

    req.method = 'DELETE'
    req.user = AnonymousUser()

    perm = PostPermission()
    assert not perm.has_object_permission(req, mock.Mock(), Post())


@pytest.mark.django_db
def test_delete_instance_if_authenticated_not_author(req):

    req.method = 'DELETE'
    req.user = User()

    post = mixer.blend(Post)

    perm = PostPermission()
    assert not perm.has_object_permission(req, mock.Mock(), post)


@pytest.mark.django_db
def test_delete_instance_if_authenticated_is_author(req):

    post = mixer.blend(Post)

    req.method = 'DELETE'
    req.user = post.author

    perm = PostPermission()
    assert perm.has_object_permission(req, mock.Mock(), post)
