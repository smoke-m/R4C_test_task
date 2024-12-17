from datetime import datetime, timedelta

from django.conf import settings
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import RobotSerializer
from .utils import get_xls_file
from robots.models import Robot


class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

    @action(detail=False, url_path="download_file", methods=("get",))
    def download_file(self, request):
        queryset = Robot.objects.filter(
            created__gte=datetime.today() - timedelta(days=settings.INTERVAL)
        ).values_list("model", "version")
        return get_xls_file(queryset)
