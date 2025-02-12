from estoque_api.estoque.managers.estoque_entrada_manager import EstoqueEntradaManager
from estoque_api.estoque.models.estoque_model import Estoque


class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = "registro de entrada de estoque"
        verbose_name_plural = "registros de entrada de estoque"
