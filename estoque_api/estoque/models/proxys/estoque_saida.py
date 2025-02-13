from estoque_api.estoque.managers.estoque_saida_manager import EstoqueSaidaManager
from estoque_api.estoque.models.estoque_model import Estoque


class EstoqueSaida(Estoque):
    objects = EstoqueSaidaManager()

    class Meta:
        proxy = True
        verbose_name = "registro de saída de estoque"
        verbose_name_plural = "registros de saída de estoque"
