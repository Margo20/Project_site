from django.contrib import admin
from .models import contactsModel, FooterModel, ExtendUser, DiscountModel, OrderCalculationModel, KapRemModel, \
    EuroRemModel, OurworkModel, RepairsModel
from django.utils.safestring import mark_safe


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'description', 'published']
    search_fields = ['published']


class FooterAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'published']
    search_fields = ['published']


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['phone', 'published']
    search_fields = ['published']


class OrderCalculationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'description', 'published']
    search_fields = ['published']


class KapRemAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'description', 'published']
    search_fields = ['published']


class EuroRemAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'description', 'published']
    search_fields = ['published']


class OurWorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_show', 'repair', 'price']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' /".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"


class RepairsAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(contactsModel, ContactAdmin)
admin.site.register(FooterModel, FooterAdmin)
admin.site.register(ExtendUser)
admin.site.register(DiscountModel, DiscountAdmin)
admin.site.register(OrderCalculationModel, OrderCalculationAdmin)
admin.site.register(KapRemModel, KapRemAdmin)
admin.site.register(EuroRemModel, EuroRemAdmin)
admin.site.register(OurworkModel, OurWorkAdmin)
admin.site.register(RepairsModel, RepairsAdmin)
