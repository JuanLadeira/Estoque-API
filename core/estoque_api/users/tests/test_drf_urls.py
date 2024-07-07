from django.urls import resolve
from django.urls import reverse
import pytest
from estoque_api.users.models import User


@pytest.mark.django_db()
def test_user_detail(user: User):
    assert (
        reverse("api:user-detail", kwargs={"username": user.username})
        == f"/api/users/{user.username}/"
    )
    assert resolve(f"/api/users/{user.username}/").view_name == "api:user-detail"


@pytest.mark.django_db()
def test_user_list():
    assert reverse("api:user-list") == "/api/users/"
    assert resolve("/api/users/").view_name == "api:user-list"


@pytest.mark.django_db()
def test_user_me():
    assert reverse("api:user-me") == "/api/users/me/"
    assert resolve("/api/users/me/").view_name == "api:user-me"
