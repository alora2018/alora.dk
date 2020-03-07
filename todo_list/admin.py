from django.contrib import admin
from .models import Vaskelist
from . import models
from django.utils.html import format_html


class OpretetTodayArchiveView(admin.TabularInline):
    inline = [Vaskelist]
    

class VaskelistAdmin(admin.ModelAdmin):
    
    #ordering = ['end_date', 'start_date']
    date_hierarchy = 'timestamp'
    fields = ['start_date', 'end_date', 'bus', 'Program', 'Kommentar', 'completed']
    #list_filter = ['start_date', 'end_date']
    #radio_fields = {"Program": admin.HORIZONTAL}
    list_editable = ['bus', 'end_date', 'Program', 'Kommentar']
    list_display = ['start_date', 'end_date', 'bus', 'Program', 'Kommentar', 'completed']
    #search_fields = ['item', 'completed']


admin.site.register(Vaskelist, VaskelistAdmin)

admin.site.site_header = 'BUSVASK - LARSENBUS & CO.'
admin.site.index_title = 'GONBUS BUSWASH'