from django.db import models
from django_jalali.db.models import jDateField
from django.contrib.auth.models import User


class koodak(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    family=models.CharField(max_length=250)
    cod_meli=models.IntegerField()
    mahal_tavalod=models.CharField(max_length=250)
    datetime=jDateField()
    namepedar=models.CharField(max_length=250)
    tahsilatpedar = models.CharField(max_length=250)
    shoghlepedar = models.CharField(max_length=250)
    telpedar = models.IntegerField()
    adress_p = models.CharField(max_length=250)
    namemadar=models.CharField(max_length=250)
    tahsilatmadar=models.CharField(max_length=250)
    shoghlmadar=models.CharField(max_length=250)
    telmadar=models.IntegerField()
    telsabet=models.CharField(max_length=250)
    adress_m= models.CharField(max_length=250)
    adressmanzel = models.CharField(max_length=250 )
    codeposti=models.IntegerField()
    vatsap=models.IntegerField()
    imagk = models.ImageField(upload_to="files/koodak" )
class personel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    family=models.CharField(max_length=250)
    cod_meli=models.IntegerField()
    mahal_tavalod=models.CharField(max_length=250)
    datetime=jDateField()
    mizantahsilat=models.CharField(max_length=250)
    reshtetahsili = models.CharField(max_length=250)
    doreamozeshi = models.CharField(max_length=400)
    sabeghekar = models.CharField(max_length=200)

    savabeghshoghli = models.CharField(max_length=400)
    semat = models.CharField(max_length=250)

    elattarkkar = models.CharField(max_length=400)
    semataknon = models.CharField(max_length=250)
    tahol=models.CharField(max_length=250)
    namehamsar=models.CharField(max_length=250)
    tedadfarzand=models.CharField(max_length=200)
    tel=models.IntegerField()
    telsabet=models.IntegerField()
    adress_m= models.CharField(max_length=250)
    imagp=models.ImageField(upload_to="files/personel")

class contactus(models.Model):


    id = models.AutoField(primary_key=True)
    namefull=models.CharField(max_length=250,verbose_name="نام کامل")
    email=models.EmailField(max_length=250)
    ip = models.CharField(max_length=50, null=True)
    masg = models.CharField(max_length=50, null=True)
    class Meta:
        verbose_name="نظر "
        verbose_name_plural="نظرات"
class ask(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    title=models.CharField(null=False,max_length=2000)
    caption=models.CharField(null=False,max_length=2000)

    created=models.DateTimeField()
    class Meta:
        verbose_name="سوال "
        verbose_name_plural="سوال ها"
class commentask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ask = models.ForeignKey(ask, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    text = models.CharField(null=False, max_length=2000)
    created = models.DateTimeField()

    class Meta:
        verbose_name = "جواب سوال ها "
        verbose_name_plural = "جواب ها"
class films(models.Model):
    name=models.CharField(max_length=200)

    film = models.FileField(upload_to="files/film",)        

class veblog(models.Model):


    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=250,verbose_name="نام کامل")
    post=models.CharField(max_length=250)
   
    class Meta:
        verbose_name="وبلاگ "
        verbose_name_plural="جزیات وبلاگ"
class clas(models.Model):


    id = models.AutoField(primary_key=True)
    nameclas=models.CharField(max_length=250,verbose_name="نام کلاس")
    namemorabi=models.CharField(max_length=250)
    roz = models.CharField(max_length=50)
    time = models.TimeField((""), auto_now=False, auto_now_add=False,max_length=50)
  
    class Meta:
        verbose_name=" کلاس"
        verbose_name_plural="کلاس ها"
class clasmodel(models.Model):


    id = models.AutoField(primary_key=True)
    nameclas=models.CharField(max_length=250,verbose_name="نام کلاس")
    namemorabi=models.CharField(max_length=250)
    roz = models.CharField(max_length=50)
    time = models.TimeField( auto_now=False, auto_now_add=False,max_length=50)
    age= models.IntegerField()
    price= models.IntegerField()
    tedad_jalasat=models.CharField(max_length=50,null=True)
    datetime=jDateField()
    class Meta:
        verbose_name=" کلاس"
        verbose_name_plural="کلاس ها"
class veblogp(models.Model):
    id=models.AutoField(primary_key=True)
    clasmodel = models.ForeignKey(clasmodel, on_delete=models.CASCADE)
    personel = models.ForeignKey(personel, on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    post=models.CharField(max_length=250)

    

######################################################################
class imageModel(models.Model):
    image=models.ImageField(upload_to="files/image")
    filter_choice=models.CharField(max_length=200)
    alt_text=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.filter_choice
        
