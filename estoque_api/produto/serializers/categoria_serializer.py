from rest_framework import serializers

from estoque_api.produto.models.categoria_model import Categoria
from estoque_api.produto.serializers.inlines.produto_inline_serializer import (
    ProdutosInlineSerializer,
)


class CategoriaGetSerializer(serializers.ModelSerializer):
    produtos = ProdutosInlineSerializer(many=True)

    class Meta:
        fields = "__all__"
        model = Categoria

class CategoriaPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Categoria
