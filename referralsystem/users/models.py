from django.db import models


class User(models.Model):
    """Класс пользователя"""
    phone_number = models.IntegerField(
        verbose_name='Номер телефона',
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

    class Meta:
        verbose_name = 'Приглашенный пользователь'
        verbose_name_plural = 'приглашенные пользователи'

    def __str__(self):
        return (f'Пользователь {self.user_who_invite.phone_number} '
                f'пригласил {self.invited_user.phone_number}')
