# Generated by Django 4.2.20 on 2025-04-25 22:00

from django.db import migrations, models
import facetest.models


class Migration(migrations.Migration):

    dependencies = [
        ("facetest", "0003_facetestmodel_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="facetestmodel",
            name="intro_image",
            field=models.ImageField(
                blank=True,
                help_text="권장 크기: 500x500px, 테스트 시작 페이지에 표시됩니다.",
                null=True,
                upload_to=facetest.models.test_image_upload_path,
                verbose_name="인트로 이미지",
            ),
        ),
    ]
