import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        help_text="Введите название категории",
                        max_length=100,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "name",
                    models.CharField(
                        help_text="Введите наименование товара",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Вставьте изображение товара",
                        null=True,
                        upload_to="product/image",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.CharField(
                        help_text="Введите цену товара",
                        max_length=100,
                        verbose_name="Цена",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату создания",
                        null=True,
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату последнего изменения",
                        null=True,
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "description",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите описание товара",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="catalog",
                        to="catalog.category",
                        verbose_name="Описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ["description", "name"],
            },
        ),
    ]