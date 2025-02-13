from rest_framework import mixins
from rest_framework import viewsets


class CreateListRetriveModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Esta classe é um viewset customizado que implementa as operações:
    - Create
    - List
    - Retrieve
    """
