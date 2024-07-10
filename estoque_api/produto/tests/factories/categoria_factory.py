from factory import Faker
from factory.django import DjangoModelFactory

from estoque_api.produto.models.categoria_model import Categoria


class CategoriaFactory(DjangoModelFactory):
    class Meta:
        model = Categoria

    categoria = Faker("word")
