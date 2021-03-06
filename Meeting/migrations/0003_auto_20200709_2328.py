# Generated by Django 3.0.6 on 2020-07-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0002_meeting_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='latitude',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='longitude',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
