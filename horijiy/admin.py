from django.contrib import admin
from .models import Horijiy

class HorijiyAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'masul_vakil', 'tuman', 'loyiha_quvvati', 'boshi', 
        'tugashi', 'loyiha_qiymati', 'pdf_file', 'excel_file', 'status', 'Kiritilgan', 'create_by'
    )
    list_filter = ('status', 'tuman', 'soha_yonalishi', 'tugatish_sanasi', 'davlat', 'update')
    search_fields = ('title', 'body', 'masul_vakil', 'loyiha_quvvati', 'davlat', 'loyiha_qiymati')

    def Kiritilgan(self, obj):
        return obj.create_at.strftime("%d.%m.%Y")  # Siz istalgan formatni qo'shing
        
    def tugashi(self, obj):
        return obj.tugatish_sanasi.strftime("%Y")  # Siz istalgan formatni qo'shing
    
    def boshi(self, obj):
        return obj.boshlash_sanasi.strftime("%Y")  # Siz istalgan formatni qo'shing
    

admin.site.register(Horijiy, HorijiyAdmin)
