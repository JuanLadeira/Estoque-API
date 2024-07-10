from rest_framework import serializers

from estoque_api.produto.models.categoria_model import Categoria


class CategoriaInlineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Categoria
