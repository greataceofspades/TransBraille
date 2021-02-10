from django.contrib import admin
from app_translator.models import BrailleText
# Register your models here.

class BrailleTextAdmin(admin.ModelAdmin):
  pass

admin.site.register(BrailleText, BrailleTextAdmin)
