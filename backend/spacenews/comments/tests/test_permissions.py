import pytest

from unittest import mock

from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

from mixer.backend.django import mixer

from comments.models import Comment
from comments.permissions import CommentPermission

User = get_user_model()


@pytest.fixture
def req():
    return HttpRequest()


def test_get_all_if_anonymous(req):

    req.method = 'GET'
    req.user = AnonymousUser()

    perm = CommentPermission()
    assert perm.has_permission(req, mock.Mock())


def test_get_all_if_authenticated(req):

    req.method = 'GET'
    req.user = User()

    perm = CommentPermission()
    assert perm.has_permission(req, mock.Mock())


def test_post_if_anonymous(req):

    req.method = 'POST'
    req.user = AnonymousUser()

    perm = CommentPermission()
    assert not perm.has_permission(req, mock.Mock())


def test_post_if_authenticated(req):

    req.method = 'POST'
    req.user = User()

    perm = CommentPermission()
    assert perm.has_permission(req, mock.Mock())


def test_get_instance_if_anonymous(req):

    req.method = 'GET'
    req.user = AnonymousUser()

    perm = CommentPermission()
    assert perm.has_object_permission(req, mock.Mock(), Comment())


def test_get_instance_if_authenticated(req):

    req.method = 'GET'
    req.user = User()

    perm = CommentPermission()
    assert perm.has_object_permission(req, mock.Mock(), Comment())


def test_put_instance_if_anonymous(req):

    req.method = 'PUT'
    req.user = AnonymousUser()

    perm = CommentPermission()
    assert not perm.has_object_permission(req, mock.Mock(), Comment())


@pytest.mark.django_db
def test_put_instance_if_authenticated_not_author(req):

    req.method = 'PUT'
    req.user = User()

    comment = mixer.blend(Comment)

    perm = CommentPermission()
    assert not perm.has_object_permission(req, mock.Mock(), comment)


@pytest.mark.django_db
def test_put_instance_if_authenticated_is_author(req):

    comment = mixer.blend(Comment)

    req.method = 'PUT'
    req.user = comment.author

    perm = CommentPermission()
    assert perm.has_object_permission(req, mock.Mock(), comment)


def test_delete_instance_if_anonymous(req):

    req.method = 'DELETE'
    req.user = AnonymousUser()

    perm = CommentPermission()
    assert not perm.has_object_permission(req, mock.Mock(), Comment())


@pytest.mark.django_db
def test_delete_instance_if_authenticated_not_author(req):

    req.method = 'DELETE'
    req.user = User()

    comment = mixer.blend(Comment)

    perm = CommentPermission()
    assert not perm.has_object_permission(req, mock.Mock(), comment)


@pytest.mark.django_db
def test_delete_instance_if_authenticated_is_author(req):

    comment = mixer.blend(Comment)

    req.method = 'DELETE'
    req.user = comment.author

    perm = CommentPermission()
    assert perm.has_object_permission(req, mock.Mock(), comment)
