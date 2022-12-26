# Generated by Django 4.0.4 on 2022-12-26 12:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_alter_application_answer1_alter_application_answer10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='generation',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
