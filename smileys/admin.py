from django.contrib import admin
from smileys.models import Smiley

class SmileyAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'description', 'image', 'is_regex', 'is_active')
    list_fileter = ('is_regex', 'is_active')
    search_fields = ('pattern', 'description', 'image')

admin.site.register(Smiley, SmileyAdmin)