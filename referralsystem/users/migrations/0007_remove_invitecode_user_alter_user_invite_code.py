# Generated by Django 5.0.4 on 2024-04-21 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_invitecode_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitecode',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.ForeignKey(max_length=6, on_delete=django.db.models.deletion.CASCADE, related_name='inv_code', to='users.invitecode', verbose_name='Код приглашения'),
        ),
    ]