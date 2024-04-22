import string
import random

from django.db import models


class User(models.Model):
    """Класс пользователя"""
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        max_length=11,
        unique=True,
        blank=False,
        null=False
    )
    invite_code = models.CharField(
        'Код',
        max_length=6,
        unique=True,
        null=False,
        blank=True
    )
    someone_invite_code = models.CharField(
        'Код-приглашение от пользователя',
        max_length=6,
        null=True,
        blank=True
    )
    invited_users = models.ManyToManyField(
        'self',
        through='InvitedUsers',
        verbose_name='Приглашенные пользователи'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.phone_number}'


class InvitedUsers(models.Model):
    user_who_invite = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_who_invite',
        null=True
    )
    invited_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='invited_user',
        null=True
    )

    def __str__(self):
        return f'Пользователь {self.user_who_invite.phone_number} пригласил {self.invited_user.phone_number}'