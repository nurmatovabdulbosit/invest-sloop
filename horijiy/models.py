from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

STATUS = (
    ('active', 'Jarayonda'),
    ('deactive', 'Tugatilgan'),
    ('expired', 'Muddati o`tgan')
)

TUMANLAR = (
    ('Namangan_shahar', 'Namangan shahar'),
    ('Davlatobod','Davlatobod'),
    ('Yangi Namangan', 'Yangi Namangan'),
    ('Mingbuloq', 'Mingbuloq'),
    ('Kosonsoy', 'Kosonsoy'),
    ('Namangan','Namangan'),
    ('Norin','Norin'),
    ('Pop','Pop'),
    ('To`raqo`rg`on','To`raqo`rg`on'),
    ('Uychi','Uychi'),
    ('Uchqo`rg`on','Uchqo`rg`on'),
    ('Chortoq','Chortoq'),
    ('Chust','Chust'),
    ('Yangiqo`rg`on', 'Yangiqo`rg`on')
)

SOHA_YONALISHLARI = (
    ('Xizmat', 'Xizmat'),
    ('Sanoat', 'Sanoat'),
    ('Qishloq', 'Qishloq'),
)


    
class Horijiy(models.Model):
    title = models.CharField(max_length=250, verbose_name="Loyiha nomi")
    slug = AutoSlugField(populate_from='title', unique=True)
    body = models.TextField()


    status = models.CharField(max_length=100, choices=STATUS, verbose_name="Holati")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan sana")
    update = models.DateTimeField(auto_now=True, verbose_name="O'zagrtirilgan")
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    masul_vakil = models.CharField(max_length=250, choices=[
        ('A.Abdurazakov', 'Sh.Abdurazzaqov'), ('A.Abduhakimov', 'A.Abduhakimov'), ('O.Inamov', 'O.Inamov')])
    tuman = models.CharField(max_length=100, choices=TUMANLAR)
    loyiha_quvvati = models.CharField(max_length=250)
    boshlash_sanasi = models.DateField(default='2024-01-01', verbose_name="Boshlash")
    tugatish_sanasi = models.DateField(default='2024-01-01', verbose_name="Tugatish")
    davlat = models.CharField(max_length=250)
    soha_yonalishi = models.CharField(max_length=100, choices=SOHA_YONALISHLARI)
    loyiha_qiymati = models.IntegerField(default=0)
    pdf_file = models.FileField(upload_to='pdf/%Y/', verbose_name="Tasdiqlangani")
    excel_file = models.FileField(upload_to='excel/%Y/', verbose_name="Tarmoq jadvali")

    def __str__(self):
        return self.title
