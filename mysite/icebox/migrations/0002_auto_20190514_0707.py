# Generated by Django 2.0.13 on 2019-05-14 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icebox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.CharField(max_length=16),
        ),
    ]