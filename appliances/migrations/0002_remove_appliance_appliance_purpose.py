# Generated by Django 4.1.1 on 2022-10-05 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliance',
            name='appliance_purpose',
        ),
    ]