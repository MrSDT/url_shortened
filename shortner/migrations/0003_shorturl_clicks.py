# Generated by Django 4.1.6 on 2023-03-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_shorturl_delete_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]
