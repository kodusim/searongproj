# Generated by Django 4.2.20 on 2025-04-25 20:53

from django.db import migrations, models
import django.db.models.deletion
import facetest.models


class Migration(migrations.Migration):

    dependencies = [
        ("facetest", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FaceResultType",
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
                ("type_id", models.IntegerField(verbose_name="유형 ID")),
                ("name", models.CharField(max_length=100, verbose_name="유형 이름")),
                ("description", models.TextField(verbose_name="설명")),
                (
                    "characteristics",
                    models.TextField(
                        help_text="특성 목록을 JSON 형식으로 저장",
                        verbose_name="특성(JSON)",
                    ),
                ),
                (
                    "examples",
                    models.TextField(
                        blank=True,
                        help_text="예시 목록을 JSON 형식으로 저장",
                        verbose_name="예시(JSON)",
                    ),
                ),
                (
                    "face_test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="result_types",
                        to="facetest.facetestmodel",
                        verbose_name="테스트",
                    ),
                ),
            ],
            options={
                "verbose_name": "얼굴상 결과 유형",
                "verbose_name_plural": "얼굴상 결과 유형",
                "ordering": ["face_test", "type_id"],
                "unique_together": {("face_test", "type_id")},
            },
        ),
        migrations.CreateModel(
            name="FaceResultImage",
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
                (
                    "image",
                    models.ImageField(
                        upload_to=facetest.models.result_image_upload_path,
                        verbose_name="이미지",
                    ),
                ),
                (
                    "title",
                    models.CharField(blank=True, max_length=100, verbose_name="제목"),
                ),
                ("order", models.PositiveIntegerField(default=0, verbose_name="순서")),
                (
                    "is_main",
                    models.BooleanField(default=False, verbose_name="대표 이미지"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                (
                    "result_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="facetest.faceresulttype",
                        verbose_name="결과 유형",
                    ),
                ),
            ],
            options={
                "verbose_name": "얼굴상 결과 이미지",
                "verbose_name_plural": "얼굴상 결과 이미지",
                "ordering": ["result_type", "order", "id"],
            },
        ),
    ]
