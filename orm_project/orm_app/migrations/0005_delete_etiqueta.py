# Generated by Django 5.0.6 on 2024-06-01 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0004_alter_etiqueta_productos_delete_producto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Etiqueta',
        ),
    ]
