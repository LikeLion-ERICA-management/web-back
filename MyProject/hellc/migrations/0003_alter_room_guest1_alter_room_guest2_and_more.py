# Generated by Django 4.1.4 on 2022-12-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hellc', '0002_calendar_is_recording_calendar_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guest1',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='room',
            name='guest2',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='room',
            name='guest3',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='room',
            name='guest4',
            field=models.IntegerField(default=-1),
        ),
    ]