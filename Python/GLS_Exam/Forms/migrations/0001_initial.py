# Generated by Django 5.0.1 on 2024-10-14 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileRegister',
            fields=[
                ('Mobile_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Mobile_Name', models.CharField(max_length=20)),
                ('Mobile_Ram', models.CharField(max_length=20)),
                ('Mobile_Price', models.CharField(max_length=20)),
                ('Mobile_Battery', models.CharField(max_length=20)),
                ('Mobile_Final_Price', models.IntegerField()),
            ],
        ),
    ]
