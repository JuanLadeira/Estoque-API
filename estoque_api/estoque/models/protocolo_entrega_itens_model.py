from django.db import models

from estoque_api.estoque.models.protocolo_entrega_model import ProtocoloEntrega
from estoque_api.produto.models.produto_model import Produto


class ProtocoloEntregaItens(models.Model):
    protocolo_entrega = models.ForeignKey(
        ProtocoloEntrega,
        on_delete=models.CASCADE,
        related_name="protocolo_entrega_itens",
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.pk} - {self.protocolo_entrega.pk} - {self.produto}"
