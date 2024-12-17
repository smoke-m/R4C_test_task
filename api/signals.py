from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from robots.models import Robot


@receiver(post_save, sender=Robot)
def robot_model_signal(sender, instance, created, **kwargs):
    if created:
        order_obj = Order.objects.filter(
            completed=False, robot_serial=instance.serial
        ).first()
        if order_obj:
            send_mail(
                "Robots.",
                settings.EMAIL.format(instance.model, instance.version),
                "example@example.com",
                [
                    order_obj.customer,
                ],
                fail_silently=False,
            )
            Order.objects.filter(id=order_obj.id).delete()  # в pr опишу


@receiver(post_save, sender=Order)
def order_model_signal(sender, instance, created, **kwargs):
    if created:
        robot_obj = Robot.objects.filter(
            in_stock=True, serial=instance.robot_serial
        ).first()
        if robot_obj:
            Robot.objects.filter(id=robot_obj.id).update(in_stock=False)
            Order.objects.filter(id=instance.id).update(completed=True)
