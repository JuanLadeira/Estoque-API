from django.utils import timezone
from factory import Faker
from factory import LazyFunction
from factory import SubFactory
from factory.django import DjangoModelFactory

from estoque_api.produto.models.produto_model import Produto
from estoque_api.produto.tests.factories.categoria_factory import CategoriaFactory


class ProdutoFactory(DjangoModelFactory):
    class Meta:
        model = Produto

    importado = Faker("boolean")
    ncm = Faker("numerify", text="########")
    produto = Faker("word")
    preco = Faker("random_number", digits=2)
    estoque = Faker("random_number", digits=2)
    estoque_minimo = Faker("random_number", digits=2)
    data = LazyFunction(timezone.now)

    categoria = SubFactory(CategoriaFactory)
