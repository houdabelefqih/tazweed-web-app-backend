# Generated by Django 2.2.8 on 2020-06-06 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200606_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='reservations',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='appointments',
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
