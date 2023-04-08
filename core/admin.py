from django.contrib import admin
from .models import *


@admin.register(Diler)
class DilerAdmin(admin.ModelAdmin):
    list_display = ['user', 'fullName', 'email', 'phone', 'address', 'seller_code', 'last_login']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'count', 'price', 'price_of_bonus']


@admin.register(ShapeSystem)
class ShapeSystemAdmin(admin.ModelAdmin):
    list_display = ['name', 'warm_proofing', 'sound_proofing', 'camera', 'shape_width', 'shape_height', 'width_glaze', 'warm_proofing_dc', 'sound_proofing_dc']


@admin.register(Implement)
class ImplementAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Glazing)
class GlazingAdmin(admin.ModelAdmin):
    list_display = ['articul']


@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ['fr', 'to', 'select','unit','count']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['zone', 'region', 'price']



@admin.register(Employ)
class EmployAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'role', 'phone', 'email']


@admin.register(Offers)
class OffersAdmin(admin.ModelAdmin):
    list_display = ['shape', 'implement', 'glazing', 'size', 'price']


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['date', 'title']


@admin.register(Instructions)
class InstructionsAdmin(admin.ModelAdmin):
    list_display = ['date', 'title']



@admin.register(Learn)
class LearnAdmin(admin.ModelAdmin):
    list_display = ['date', 'title']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['date', 'title']



@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['date', 'title']


admin.site.register(Role)


admin.site.register(Sample)
