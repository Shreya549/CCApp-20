# Generated by Django 3.0.6 on 2020-07-26 14:21

import Reimbursements.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reimbursements', '0002_auto_20200704_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill',
            field=models.ImageField(blank=True, null=True, upload_to=Reimbursements.models.path_and_rename),
        ),
        migrations.AlterField(
            model_name='bill',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
