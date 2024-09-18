from django.urls import path
from network.apps import NetworkConfig
from network.views import LinkListAPIView, LinkCreateAPIView, LinkDestroyView, LinkRetrieveView, LinkUpdateView, ProductViewSet
from rest_framework.routers import DefaultRouter


app_name = NetworkConfig.name

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('network/create/', LinkCreateAPIView.as_view(), name='network-create'),
    path('network/list/', LinkListAPIView.as_view(), name='network-list'),
    path('network/<int:pk>/', LinkRetrieveView.as_view(), name='network-get'),
    path('network/<int:pk>/update/', LinkUpdateView.as_view(), name='network-update'),
    path('network/<int:pk>/delete/', LinkDestroyView.as_view(), name='network-delete'),
] + router.urls
