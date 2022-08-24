from django.contrib import admin

# Register your models here.


from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email','subject','phone','date','message')
    list_filter=('date','subject')


admin.site.register(Contact_u, ContactAdmin)


