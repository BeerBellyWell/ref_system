from django.contrib import admin
from users.models import User, InviteCode


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'phone_number', 'invite_code', 'someone_invite_code',
        )
    
    def get_invited_users(self, obj):
        return '\n'.join([i.phome_number for i in obj.invited_users.all()])
    

class InviteCodeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'code'
    )


admin.site.register(User, UserAdmin)
admin.site.register(InviteCode, InviteCodeAdmin)
