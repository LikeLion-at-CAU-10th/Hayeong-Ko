from django.contrib import admin
from .models import LikeLion
# Register your models here.

@admin.register(LikeLion)
class LikeLionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'part', 'age', 'bio')
    list_editable = ('bio', )
    list_filter = ('part', )
    search_fields = ('id', 'name', 'part')
    