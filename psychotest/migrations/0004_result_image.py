# Generated by Django 4.2.20 on 2025-04-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("psychotest", "0003_test_image_test_view_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="권장 크기: 400x400",
                null=True,
                upload_to="result_images/",
                verbose_name="결과 이미지",
            ),
        ),
    ]
