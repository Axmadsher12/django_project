from django.contrib import admin
from mpfiles.models import Viloyatlar,Bemorlar_baza
# Register your models here.
class Viloyatlar_admin(admin.ModelAdmin):
    list_display = ["id",
                    "nomi"]
admin.site.register(Viloyatlar,Viloyatlar_admin)
"------------------------------------------------------------------------------------------------------------------"
class Bemorlar_admin(admin.ModelAdmin):
    list_display = ["id",
                    "Ism",
                    "Familiya",
                    "Otasini_ismi",
                    "Viloyat",
                    "Shahar_yoki_tuman",
                    "Mahallas",
                    "Kocha",
                    "Uy_raqam",
                    "Tugilgan_sana",
                    "Bolim_nomi",
                    "Kimning_qabulida",
                    "Telefon",
                    "Qoshimch_malumot",
                    "Kelgan_sanasi"]
admin.site.register(Bemorlar_baza,Bemorlar_admin)
