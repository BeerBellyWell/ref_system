# Generated by Django 5.0.4 on 2024-04-21 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_invite_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv_code', to='users.invitecode', verbose_name='Код приглашения'),
        ),
    ]