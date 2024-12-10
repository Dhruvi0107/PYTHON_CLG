# Generated by Django 5.0.1 on 2024-08-03 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Emp_ID', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(max_length=20)),
                ('Salary', models.IntegerField()),
                ('Date_Of_Join', models.DateField()),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.employee')),
            ],
        ),
    ]