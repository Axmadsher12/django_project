from django.db import models


# Create your models here.
class Viloyatlar(models.Model):
    nomi = models.CharField(max_length=20)
    def __str__(self):
        return self.nomi


class Bemorlar_baza(models.Model):
    Ism = models.CharField(max_length=20)
    Familiya = models.CharField(max_length=20)
    Otasini_ismi = models.CharField(max_length=20)
    Viloyat = models.ForeignKey(Viloyatlar, on_delete=models.CASCADE)
    Shahar_yoki_tuman = models.CharField(max_length=20)
    Mahallas = models.CharField(max_length=20)
    Kocha = models.CharField(max_length=20)
    Uy_raqam = models.IntegerField()
    Tugilgan_sana = models.DateField(default='')
    Bolim_nomi = models.CharField(max_length=20)
    Kimning_qabulida = models.CharField(max_length=20)
    Telefon = models.IntegerField()
    Qoshimch_malumot = models.CharField(max_length=30)
    Kelgan_sanasi = models.DateField(auto_now=True)
