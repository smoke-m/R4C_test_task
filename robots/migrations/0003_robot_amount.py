# Generated by Django 4.2 on 2024-12-16 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("robots", "0002_robotmodel_alter_robot_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="robot",
            name="amount",
            field=models.PositiveSmallIntegerField(default=2),
            preserve_default=False,
        ),
    ]
