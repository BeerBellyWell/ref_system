# Generated by Django 5.0.4 on 2024-04-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_user_invited_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='invited_users',
            field=models.ManyToManyField(through='users.InvitedUsers', to='users.user', verbose_name='Приглашенные пользователи'),
        ),
    ]