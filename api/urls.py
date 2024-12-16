from django.urls import include, path
from rest_framework import routers

from .views import RobotViewSet

app_name = "api"

router_v1 = routers.DefaultRouter()
router_v1.register("robots", RobotViewSet, basename="robots")

urlpatterns = [
    path("", include(router_v1.urls)),
]