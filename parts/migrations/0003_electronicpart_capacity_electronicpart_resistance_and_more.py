# Generated by Django 4.1.1 on 2022-11-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parts", "0002_part_to_buy"),
    ]

    operations = [
        migrations.AddField(
            model_name="electronicpart",
            name="capacity",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="electronicpart",
            name="resistance",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="electronicpart",
            name="tolerance",
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="part",
            name="price",
            field=models.FloatField(blank=True),
        ),
    ]
