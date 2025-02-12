from django.db import models


class EstoqueEntradaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(movimento="e")
