from django.contrib import admin

# Register your models here.

from .models import *


class ApplicantAdmin(admin.ModelAdmin):


    list_display=('firstname', 'lastname', 'email', 'phone','address','course','center','mode')

    list_filter=('firstname', 'lastname','address','course','center', 'date')



admin.site.register(Applicants, ApplicantAdmin)