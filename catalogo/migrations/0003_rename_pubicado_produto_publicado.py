# Generated by Django 4.0.2 on 2022-02-19 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_produto_pubicado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='pubicado',
            new_name='publicado',
        ),
    ]
