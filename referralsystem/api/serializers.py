import string
import random

from rest_framework import serializers

from users.models import User, InvitedUsers


def generate_code():
    chars = string.ascii_uppercase + string.digits
    gen_invite_code = ''.join(random.choice(chars) for i in range(6))
    while User.objects.filter(invite_code=gen_invite_code).exists():
        gen_invite_code = ''.join(random.choice(chars) for i in range(6))
    return gen_invite_code


class UserSerializer(serializers.ModelSerializer):
    invite_code = serializers.StringRelatedField(read_only=True)
    invited_users = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone_number', 'invite_code', 'someone_invite_code',
                  'invited_users'
                  )

    def create(self, validated_data):
        gen_invite_code = generate_code()

        if 'someone_invite_code' not in self.initial_data:
            user = User.objects.create(
                **validated_data,
                invite_code=gen_invite_code,
            )
            return user

        someone_invite_code = validated_data.pop('someone_invite_code')

        user_who_inv = User.objects.filter(invite_code=someone_invite_code)
        if user_who_inv.exists():
            user = User.objects.create(
                **validated_data,
                invite_code=gen_invite_code,
                someone_invite_code=someone_invite_code
                )
            get_user_who_inv = user_who_inv.get()
            InvitedUsers.objects.create(
                user_who_invite=get_user_who_inv,
                invited_user=user
                )
            return user
        raise serializers.ValidationError(
            f'Пользователь с кодом {someone_invite_code} отсутствует'
        )

    def update(self, instance, validated_data):
        user = User.objects.get(phone_number=instance.phone_number)
        if instance.someone_invite_code:
            raise serializers.ValidationError(
                'У вас уже есть реферальный код, его нельзя поменять'
            )
        code = validated_data.pop('someone_invite_code')
        if user.invite_code == code:
            raise serializers.ValidationError(
                'Нельзя использовать свой реферальный код'
            )
        some_user = User.objects.filter(invite_code=code)
        if some_user.exists():
            instance.someone_invite_code = code
            instance.save()

            get_user_who_inv = some_user.get()
            InvitedUsers.objects.create(
                user_who_invite=get_user_who_inv,
                invited_user=user)
            return instance
        raise serializers.ValidationError(
            'Пользователя с таким кодом не существует'
        )
