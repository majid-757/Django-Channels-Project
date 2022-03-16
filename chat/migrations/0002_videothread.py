# Generated by Django 3.2 on 2022-03-16 19:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoThread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('date_started', models.DateTimeField(default=datetime.datetime.now)),
                ('date_ended', models.DateTimeField(default=datetime.datetime.now)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('callee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='callee_user', to=settings.AUTH_USER_MODEL)),
                ('caller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caller_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]