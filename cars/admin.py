from django.contrib import admin
from cars.models import Brand, Car, CarCondition, CarStatus

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'car_brand')

class CarConditionAdmin(admin.ModelAdmin):
    list_display = ('condition',)
    search_fields = ('condition',)

class CarStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarCondition, CarConditionAdmin)
admin.site.register(CarStatus, CarStatusAdmin)