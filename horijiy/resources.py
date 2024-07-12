from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Horijiy
from django.contrib.auth.models import User
from datetime import datetime

class HorijiyResource(resources.ModelResource):
    create_by = fields.Field(
        column_name='create_by',
        attribute='create_by',
        widget=ForeignKeyWidget(User, 'username')
    )

    class Meta:
        model = Horijiy
        fields = ('id', 'title', 'create_at', 'masul_vakil', 'loyiha_quvvati', 'davlat', 'soha_yonalishi', 'loyiha_qiymati', 'create_by')
        import_id_fields = ['id']

    def before_import_row(self, row, **kwargs):
        # create_at maydonini bugungi sana bilan to'ldiramiz
        if not row.get('create_at'):
            row['create_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # create_by maydonini hozirgi foydalanuvchi bilan to'ldiramiz
        user = kwargs['user']
        if not row.get('create_by'):
            row['create_by'] = user.username
