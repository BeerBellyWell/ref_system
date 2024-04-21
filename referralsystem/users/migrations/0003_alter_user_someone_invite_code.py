# Generated by Django 5.0.4 on 2024-04-21 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_slug_user_invite_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='someone_invite_code',
            field=models.ForeignKey(blank=True, max_length=6, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='some_inv_code', to='users.invitecode', verbose_name='Чужой инвайд код'),
        ),
    ]
