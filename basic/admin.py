from django.contrib import admin
from basic.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id',)

admin.site.register(User, UserAdmin)
