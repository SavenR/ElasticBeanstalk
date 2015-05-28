from django.conf.urls import url, include
from rest_framework import routers
from .api.views import ExampleViewSet

router = routers.DefaultRouter()
router.register(r'app', ExampleViewSet, base_name='app')

urlpatterns = [
    url(r'^', include(router.urls)), # Include router urls into our urlpatterns
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]