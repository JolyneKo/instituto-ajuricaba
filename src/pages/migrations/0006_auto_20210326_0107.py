# Generated by Django 3.1.7 on 2021-03-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210325_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagem',
            field=models.ImageField(upload_to='Eventos'),
        ),
    ]
