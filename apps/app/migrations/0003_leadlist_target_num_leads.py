# Generated by Django 3.2.12 on 2022-04-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_leadlist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadlist',
            name='target_num_leads',
            field=models.IntegerField(default=0),
        ),
    ]
