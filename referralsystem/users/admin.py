from django.contrib import admin
from users.models import User, InvitedUsers


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'phone_number', 'invite_code', 'someone_invite_code',
        )
    
    # def get_invited_users(self, obj):
    #     return '\n'.join([i.phome_number for i in obj.invited_users.all()])
    

class InvitedUsersAdmin(admin.ModelAdmin):
    list_display = ('user_who_invite', 'invited_user')
    

admin.site.register(User, UserAdmin)
admin.site.register(InvitedUsers, InvitedUsersAdmin)
