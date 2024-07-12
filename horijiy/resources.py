from import_export import resources
from .models import Horijiy

class HorijiyResource(resources.ModelResource):
    class Meta:
        model = Horijiy
        fields = (
            'id', 'title', 'slug', 'body', 'status', 'create_at', 
            'update', 'create_by', 'masul_vakil', 'tuman', 
            'loyiha_quvvati', 'boshlash_sanasi', 'tugatish_sanasi', 
            'davlat', 'soha_yonalishi', 'loyiha_qiymati', 'pdf_file', 'excel_file'
        )
        export_order = fields
