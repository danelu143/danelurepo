from django.contrib import admin
from newsapp.models import student
class studentAdmin(admin.ModelAdmin):
    list_display = ['sno','sname','mark']
admin.site.register(student,studentAdmin)