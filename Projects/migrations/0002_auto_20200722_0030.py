# Generated by Django 3.0.6 on 2020-07-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='NAME', max_length=100),
        ),
    ]
