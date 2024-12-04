from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CategoryViewSet, OrdersViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
router = DefaultRouter()
router.register('users', UserViewSet)

router.register('products', ProductViewSet)

router.register('categories', CategoryViewSet)

router.register('orders', OrdersViewSet)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
] 
urlpatterns += router.urls