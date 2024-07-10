from logging import getLogger

import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from estoque_api.estoque.tests.factories.estoque_entrada_factory import (
    EstoqueEntradaFactory,
)
from estoque_api.estoque.tests.factories.estoque_itens_factory import (
    EstoqueItensFactory,
)
from estoque_api.produto.tests.factories.categoria_factory import CategoriaFactory
from estoque_api.produto.tests.factories.produto_factory import ProdutoFactory
from estoque_api.users.tests.factories import UserFactory

logger = getLogger("django")


@pytest.fixture()
def api_client():
    return APIClient()


register(ProdutoFactory)
register(CategoriaFactory)
register(UserFactory)
register(EstoqueEntradaFactory)
register(EstoqueItensFactory)


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath
