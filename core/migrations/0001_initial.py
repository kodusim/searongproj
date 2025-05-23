# Generated by Django 4.2.20 on 2025-04-26 21:17

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Banner",
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
                ("title", models.CharField(max_length=100, verbose_name="제목")),
                (
                    "image",
                    models.ImageField(
                        upload_to=core.models.banner_image_path,
                        verbose_name="배너 이미지",
                    ),
                ),
                ("url", models.URLField(blank=True, verbose_name="링크 URL")),
                ("is_active", models.BooleanField(default=True, verbose_name="활성화")),
                ("order", models.PositiveIntegerField(default=0, verbose_name="순서")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록일"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정일"),
                ),
            ],
            options={
                "verbose_name": "배너",
                "verbose_name_plural": "배너 관리",
                "ordering": ["order", "-created_at"],
            },
        ),
    ]
