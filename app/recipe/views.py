from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient

from recipe import serializers


class BaseRecipeAttribute(viewsets.GenericViewSet, mixins.ListModelMixin,
                          mixins.CreateModelMixin):
    """common features for both tag and ingredients viewsets"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)


class IngredientViewSet(BaseRecipeAttribute):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class TagViewSet(BaseRecipeAttribute):
    """manage tag in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
