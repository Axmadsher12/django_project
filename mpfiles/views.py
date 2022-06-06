from django.shortcuts import render
from mpfiles.models import Bemorlar_baza,Viloyatlar
# Create your views here.
#from mpfiles.models import Bemorlar_baza

def Table(table):
    if table.method=="POST":
        B_ISM = table.POST.get('ism')
        B_FAMILIYA = table.POST.get('familiya')
        B_OTASINI_ISMI = table.POST.get('otasini_ismi')
        B_VILOYATS_ID = table.POST.get('viloyat')
        B_VILOYAT = Viloyatlar.objects.get(id=B_VILOYATS_ID)
        B_SHAHAR_YOKI_TUMAN = table.POST.get('shahar_yoki_tuman')
        B_MAHALLA = table.POST.get('mahalla')
        B_KOCHA = table.POST.get('kocha')
        B_UY_RAQAM = table.POST.get('uy_raqam')
        B_TUGILGAN_SANA = table.POST.get('tugilgan_sana')
        B_QAYSI_BOLIMGA = table.POST.get('qaysi_bolimga')
        B_KIMNING_QABULIGA = table.POST.get('kimning_qabuliga')
        B_TELEFON = table.POST.get('telefon')
        B_QOSHIMCHA_MALUMOT = table.POST.get('qoshimcha_malumot')
        B_KELGAN_SANASI = table.POST.get('Kelgan_sanasi')
        Bemorlar_baza(Ism=B_ISM,
                      Familiya=B_FAMILIYA,
                      Otasini_ismi=B_OTASINI_ISMI,
                      Viloyat=B_VILOYAT,
                      Shahar_yoki_tuman=B_SHAHAR_YOKI_TUMAN,
                      Mahallas=B_MAHALLA,
                      Kocha=B_KOCHA,
                      Uy_raqam=B_UY_RAQAM,
                      Tugilgan_sana=B_TUGILGAN_SANA,
                      Bolim_nomi=B_QAYSI_BOLIMGA,
                      Kimning_qabulida=B_KIMNING_QABULIGA,
                      Telefon=B_TELEFON,
                      Qoshimch_malumot=B_QOSHIMCHA_MALUMOT,
                      Kelgan_sanasi=B_KELGAN_SANASI
                      ).save()
    Jadval = Bemorlar_baza.objects.all().order_by('-id')
    return render(table, "Bemorlar.html", {"Jadval": Jadval})

def Add_table(table):
    Viloyat=Viloyatlar.objects.all()
    return render(table,'add_page.html',{"Viloyat_select":Viloyat})

def Update_table(table,id):
    update = Bemorlar_baza.objects.get(id=id)
    Viloyat = Viloyatlar.objects.all()
    return render(table,'Update_page.html',{'ozgartirish':update,"Viloyat_select":Viloyat})

def Delete_table(table,id):
    Delete=Bemorlar_baza.objects.get(id=id).delete()
    Jadval = Bemorlar_baza.objects.all().order_by('-id')
    return render(table, "Bemorlar.html", {"Jadval": Jadval})
