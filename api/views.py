from rest_framework import viewsets

from .serializers import RobotSerializerRead, RobotSerializerWrite
from robots.models import Robot


class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()

    def get_serializer_class(self):
        """Выбор сериализатора."""
        if self.action in ("list", "retrieve"):
            return RobotSerializerRead
        elif self.action in ("create", "partial_update"):
            return RobotSerializerWrite
