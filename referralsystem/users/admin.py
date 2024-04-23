from django.contrib import admin
from users.models import User, InvitedUsers


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'phone_number', 'invite_code', 'someone_invite_code',
        )


class InvitedUsersAdmin(admin.ModelAdmin):
    list_display = ('user_who_invite', 'invited_user')


admin.site.register(User, UserAdmin)
admin.site.register(InvitedUsers, InvitedUsersAdmin)
