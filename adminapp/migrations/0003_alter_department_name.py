# Generated by Django 4.2.2 on 2023-06-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
