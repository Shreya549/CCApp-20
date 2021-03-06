# Generated by Django 3.0.6 on 2020-07-13 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Meeting', '0003_auto_20200709_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('regno', models.CharField(max_length=10, null=True)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_attendance', to='Meeting.Meeting')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
