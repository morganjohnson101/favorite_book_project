from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'password')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'creator')
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
