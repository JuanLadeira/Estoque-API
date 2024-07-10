from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from estoque_api.estoque.views import estoque_entrada_viewset
from estoque_api.estoque.views import estoque_saida_viewset
from estoque_api.estoque.views import protocolo_entrega_viewset
from estoque_api.produto.views import categoria_viewset
from estoque_api.produto.views import produto_viewset
from estoque_api.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("produto", produto_viewset.ProdutoViewSet)
router.register("categoria", categoria_viewset.CategoriaViewSet)
router.register("estoque_saida", estoque_saida_viewset.EstoqueSaidaViewSet)
router.register("estoque_entrada", estoque_entrada_viewset.EstoqueEntradaViewSet)
router.register("protocolo_entrega", protocolo_entrega_viewset.ProtocoloEntregaViewSet)


app_name = "api"
urlpatterns = router.urls
