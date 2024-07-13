from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Horijiy
from .resources import HorijiyResource

class HorijiyAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = HorijiyResource

    list_display = (
        'title', 'masul_vakil', 'tuman', 'loyiha_quvvati', 'boshi', 
        'tugashi', 'loyiha_qiymati', 'pdf_file', 'excel_file', 'status', 'Kiritilgan', 'create_by'
    )
    list_filter = ('status', 'tuman', 'soha_yonalishi', 'tugatish_sanasi', 'davlat', 'update')
    search_fields = ('title', 'body', 'masul_vakil', 'loyiha_quvvati', 'davlat', 'loyiha_qiymati')

    def Kiritilgan(self, obj):
        return obj.create_at.strftime("%d.%m.%Y")  # Siz istalgan formatni qo'shing
    Kiritilgan.short_description = 'Kiritilgan Sana'
        
    def tugashi(self, obj):
        return obj.tugatish_sanasi.strftime("%Y")  # Siz istalgan formatni qo'shing
    tugashi.short_description = 'Tugatish Yili'
    
    def boshi(self, obj):
        return obj.boshlash_sanasi.strftime("%Y")  # Siz istalgan formatni qo'shing
    boshi.short_description = 'Boshlash Yili'

admin.site.register(Horijiy, HorijiyAdmin)
