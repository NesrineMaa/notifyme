# Generated by Django 2.2.2 on 2019-07-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifyapp', '0009_remove_url_nb_notif'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='Nb_notif',
            field=models.IntegerField(default=True),
        ),
    ]
