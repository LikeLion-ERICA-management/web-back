# Generated by Django 4.0.4 on 2022-12-27 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_alter_faq_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='opening',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
