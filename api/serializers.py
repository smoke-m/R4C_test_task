from rest_framework import serializers

from orders.models import Order
from robots.models import Robot


class RobotSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
    )

    class Meta:
        model = Robot
        fields = ("serial", "model", "version", "created")

    def to_internal_value(self, data):
        data["serial"] = "{}-{}".format(data["model"], data["version"])
        return super().to_internal_value(data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("customer", "robot_serial", "completed")
