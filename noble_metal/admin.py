from django.contrib import admin
from noble_metal.models import GoldPrice


class GoldPriceAdmin(admin.ModelAdmin):

    list_display = (
        'date', 'time', 'dtype', 'situation', 'price')
    search_fields = ['situation', ]
    # list_filter = ('name',)


# Register your models here.
admin.site.register(GoldPrice, GoldPriceAdmin)
