from django.contrib import admin
from about.models import About
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    pass

admin.site.register(About, AboutAdmin)

