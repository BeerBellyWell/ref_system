# Generated by Django 5.0.4 on 2024-04-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_invitedfusers_alter_user_invite_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.CharField(blank=True, max_length=6, unique=True, verbose_name='Код'),
        ),
    ]
