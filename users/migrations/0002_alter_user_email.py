# Generated by Django 4.0.7 on 2023-03-06 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This field must be unique.'}, max_length=127, unique=True),
        ),
    ]
