from rest_framework import serializers

from robots.models import Robot


class RobotSerializerRead(serializers.ModelSerializer):
    created = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
    )

    class Meta:
        model = Robot
        fields = ("serial", "model", "version", "created")


class RobotSerializerWrite(serializers.ModelSerializer):
    serial = serializers.SerializerMethodField()
    created = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
    )

    class Meta:
        model = Robot
        fields = ("serial", "model", "version", "created")

    def get_serial(self, obj):
        return "{}-{}".format(obj.model, obj.version)
