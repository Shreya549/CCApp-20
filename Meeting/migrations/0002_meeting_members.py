# Generated by Django 3.0.6 on 2020-07-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='members',
            field=models.CharField(default='All Core Committee Members', max_length=200),
        ),
    ]