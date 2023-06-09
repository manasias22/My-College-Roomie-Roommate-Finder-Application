# Generated by Django 4.1.5 on 2023-03-31 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_vacantroom_area_vacantroom_city_vacantroom_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacantroom',
            name='rent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vacantroom',
            name='room_mate_present',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vacantroom',
            name='room_mate_require',
            field=models.IntegerField(default=0),
        ),
    ]
