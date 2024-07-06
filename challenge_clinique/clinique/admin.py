from django.contrib import admin
from .models import Patient, Consultation, Hospitalisation, Examination, Product, Sale,Room


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'address', 'phone_number', 'consulted')
    search_fields = ('name', 'phone_number')
    list_filter = ('consulted',)


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'notes')
    search_fields = ('patient__name', 'notes')
    list_filter = ('date',)


class HospitalisationAdmin(admin.ModelAdmin):
    list_display = ('consultation', 'room', 'start_date', 'end_date')
    search_fields = ('consultation__patient__name', 'room_number')
    #list_filter = ('room_number', 'admission_date', 'discharge_date')


class ExaminationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'exam_type', 'date', 'results')
    search_fields = ('patient__name', 'exam_type', 'results')
    list_filter = ('exam_type', 'date')


class ProductAdmin(admin.ModelAdmin):
    #list_display = ('name', 'stock_quantity', 'price')
    list_display = ('name', 'stock_quantity')
    search_fields = ('name',)
    list_filter = ('stock_quantity',)


class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'date')
    search_fields = ('product__name',)
    list_filter = ('date',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')
    search_fields = ('number',)
    list_filter = ('capacity',)


admin.site.register(Patient, PatientAdmin)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Hospitalisation, HospitalisationAdmin)
admin.site.register(Examination, ExaminationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Room, RoomAdmin)