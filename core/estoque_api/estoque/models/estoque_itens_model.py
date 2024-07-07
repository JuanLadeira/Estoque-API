from django.db import models, transaction
from datetime import date
from estoque_api.estoque.exceptions import ProdutoSaldoInsuficienteError
from estoque_api.produto.models.produto_model import Produto
from estoque_api.estoque.models.estoque_model import Estoque

from logging import getLogger

log = getLogger("django")

class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoque_itens'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'item'
        verbose_name_plural = 'itens do registro de estoque'

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)


    def data(self) -> date:
        return self.estoque.data
    
    def movimento(self) -> str:
        return self.estoque.get_movimento_display()
    
    def nf(self)-> int:
        return self.estoque.nf

    @transaction.atomic
    def atualizar_saldo(self):
        """
        Atualiza o saldo do produto relacionado a este item de estoque.
        """
        if self.estoque.movimento == 'e':
            saldo = self.produto.estoque + self.quantidade
        else:
            log.info("entrei na subtração do saldo")
            saldo = self.produto.estoque - self.quantidade
            if saldo < 0:
                raise ProdutoSaldoInsuficienteError(self.produto.produto, self.quantidade)
        self.saldo = saldo
        self.produto.estoque = saldo
        self.produto.save()
        self.save()
  
