from estoque_api.users.models import User
import pytest

@pytest.mark.django_db()
def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"
