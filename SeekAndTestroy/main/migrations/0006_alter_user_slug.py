# Generated by Django 3.2.3 on 2021-07-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=150, verbose_name='Slug'),
        ),
    ]
