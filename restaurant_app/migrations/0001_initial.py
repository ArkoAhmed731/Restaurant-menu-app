# Generated by Django 5.1.3 on 2024-11-06 16:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("meal", models.CharField(max_length=1000, unique=True)),
                ("descriptions", models.CharField(max_length=2000)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "meal_type",
                    models.CharField(
                        choices=[
                            ("starters", "Starters"),
                            ("salads", "Salads"),
                            ("main_dishes", "Main Dishes"),
                            ("desserts", "Deserts"),
                        ],
                        max_length=2000,
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Unavailable"), (1, "Available")], default=0
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
