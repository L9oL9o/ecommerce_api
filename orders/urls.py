from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.views import ProductModelViewSet, OrderModelViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('order', OrderModelViewSet, 'order')


urlpatterns = [
    path('router-url/', include(router.urls)),
]
