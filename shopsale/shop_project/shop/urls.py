from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductCategoryViewSet, BasketViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', ProductCategoryViewSet, basename='categories')
router.register(r'baskets', BasketViewSet, basename='baskets')

urlpatterns = router.urls
