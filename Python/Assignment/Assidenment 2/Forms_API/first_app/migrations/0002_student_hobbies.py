# Generated by Django 5.0.1 on 2024-10-14 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Hobbies',
            field=models.CharField(default='Sports', max_length=20),
            preserve_default=False,
        ),
    ]
