# Generated by Django 2.2.2 on 2019-07-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='cat',
            field=models.CharField(max_length=200),
        ),
    ]
