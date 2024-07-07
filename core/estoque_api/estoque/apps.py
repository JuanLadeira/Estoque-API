from django.apps import AppConfig

from logging import getLogger

logger = getLogger("django")

class EstoqueConfig(AppConfig):
    name = 'estoque_api.estoque'
    default_auto_field = 'django.db.models.BigAutoField'

