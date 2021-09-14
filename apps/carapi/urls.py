from django.urls import include, path
from rest_framework import routers
from . import views
from .views import MMSViewSet, CarViewSet

app_name = "carapi"

router = routers.DefaultRouter()
router.register(r'all', MMSViewSet, basename='all_models')
router.register(r'car', CarViewSet, basename='all_car')

# added routing for two default api

urlpatterns = [
    path('', include(router.urls)),
    path('addcar/', views.ADDCarView.as_view(), name='add_car'),
    path('searchcar/', views.CarSearchView.as_view(), name='search_car'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]