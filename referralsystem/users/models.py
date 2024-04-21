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
    invite_code = models.ForeignKey(  # Onetoonefield 
        'InviteCode',
        on_delete=models.CASCADE,
        related_name='inv_code',
        verbose_name='Код приглашения',
        max_length=6,
        null=False,
        blank=False
    )
    someone_invite_code = models.ForeignKey(
        'InviteCode',
        on_delete=models.SET_NULL,
        related_name='some_inv_code',
        verbose_name='Чужой инвайд код',
        max_length=6,
        null=True,
        blank=True
    )
    invited_users = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name='Приглашенные пользователи'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.phone_number

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # Сохранить объект User

    #     if not self.invite_code:
    #         # Сгенерировать случайный код приглашения
    #         chars = string.ascii_uppercase + string.digits
    #         invite_code = ''.join(random.choice(chars) for i in range(6))

    #         # Создать объект InviteCode и связать его с пользователем
    #         InviteCode.objects.create(code=invite_code, user=self)
        

class InviteCode(models.Model):
    # user = models.ForeignKey(  # Onetoonefield 
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='code'
    # )
    code = models.CharField(
        'Код',
        max_length=6,
        unique=True
    )

    class Meta:
        verbose_name = 'Инвайт код'
        verbose_name_plural = 'Инвайт коды'

    def __str__(self):
        return self.code
