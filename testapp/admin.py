from attr import field
from django.contrib import admin
from testapp.models import *
# Register your models here.

class userAdmin(admin.ModelAdmin):
    class Meta:
        models=user
        fields='__all__'
class todoAdmin(admin.ModelAdmin):
    class Meta:
        models=Todo
        fields='__all__'
admin.site.register(user,userAdmin)
admin.site.register(Todo,todoAdmin)
