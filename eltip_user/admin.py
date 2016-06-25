from django.contrib import admin
from eltip_user.models import User, Account
class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdate', 'updatedate', 'account', 'password', \
                    'name', 'email', 'company', 'position')
class accountAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'createdate', 'updatedate', 'credit', 'balance')

admin.site.register(User, userAdmin)
admin.site.register(Account, accountAdmin)
