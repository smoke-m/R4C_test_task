from django.db import models


class RobotModel(models.Model):
    model_ind = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return self.model_ind


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.ForeignKey(
        RobotModel,
        on_delete=models.CASCADE,
        related_name="robots",
    )
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.serial
