# Generated by Django 4.1.4 on 2022-12-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hellc', '0005_alter_calendar_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('is_chest', models.BooleanField()),
                ('is_back', models.BooleanField()),
                ('is_shoulder', models.BooleanField()),
                ('gym_name', models.CharField(max_length=100)),
                ('year', models.SmallIntegerField(default=0)),
                ('month', models.SmallIntegerField(default=0)),
                ('date', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
