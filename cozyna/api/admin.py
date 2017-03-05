from django.contrib import admin
from .models import arrived, entered, finished, left, order, sat
# Register your models here.

admin.site.register(arrived)
admin.site.register(entered)
admin.site.register(finished)
admin.site.register(left)
admin.site.register(order)
admin.site.register(sat)
