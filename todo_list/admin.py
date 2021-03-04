from django.contrib import admin
from .models import *


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)



admin.site.site_header = 'BUSVASK - LARSENBUS & CO.'
admin.site.index_title = 'GONBUS BUSWASH'