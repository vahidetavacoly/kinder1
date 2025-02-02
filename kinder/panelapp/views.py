from django.shortcuts import render
from .form import imageuploadform,singup_formp, loginformp,teacher_form,kodak_form,login_form,singup_form,veblogp_form,contactusmodel,askform ,commentaskform,filmform,clas_form,veblog_form
from .models import koodak,personel,ask ,imageModel,commentask,contactus,films,veblog,clasmodel,veblogp
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .userauth import userauth
from django.shortcuts import get_object_or_404,render
import socket
from django.core import serializers
import datetime
import os
from django.utils.text import slugify


 

#####################################################################################
def about(request):
    return render(request=request, template_name="about.html")
#####################################################################################
def blog_classic(request):
    tabel=veblog.objects.all()
    form = veblog_form()  
    return render(request=request, template_name="blog-classic.html", context={"tabel": tabel, "form": form})
def blog_grid(request):
    tabel=veblog.objects.all()
    form = veblog_form()  
    return render(request=request, template_name="blog-grid.html", context={"tabel": tabel, "form": form})
def blog_single(request):
    tabel1=contactus.objects.all()
    tabel=veblog.objects.all()
    form = veblog_form()
    form1=contactusmodel() 
    return render(request=request, template_name="blog-single.html", context={"tabel": tabel, "form": form,"tabel1": tabel1, "form1": form1})
def saveveblog(request):
     if request.method == "POST":
            formsy = veblog_form(request.POST)
            us = veblog(
                title=formsy.data["title"],
                post=formsy.data["post"],   
                )
            us.save()
            return HttpResponseRedirect("/creatveblog")            
     else:
         return HttpResponse("خطا")
def creatveblog(request):
      form=veblog_form()
      return render(request=request, template_name="creatveblog.html",context={"form":form})                 
###########################################################################################
def class_schedule(request):
    tabel=clasmodel.objects.all()
    form = clas_form()  
    return render(request=request, template_name="class-schedule.html", context={"tabel": tabel, "form": form})
def class_single(request):
    tabel=clasmodel.objects.all()
    form = clas_form()  
    return render(request=request, template_name="class-single.html", context={"tabel": tabel, "form": form})
def saveclas(request):    
        if request.method == "POST":
                    formsy = clas_form(request.POST)
                    print(formsy.data)
                    us = clasmodel(
                        nameclas=formsy.data["nameclas"],
                        namemorabi=formsy.data["namemorabi"],
                        roz = formsy.data["roz"],
                        time = formsy.data["time_0"],
                        age=  formsy.data["age"],
                        price=  formsy.data["price"],
                        tedad_jalasat= formsy.data["tedad_jalasat"],
                        datetime= formsy.data["datetime"],
                        )
                    us.save()
                    return HttpResponseRedirect("/creatclas")            
        else:
                return HttpResponse("خطا")
def creatclas(request):
      form1=clas_form()
      return render(request=request, template_name="creatclas.html",context={"form1":form1})                 
def classes(request):
    tabel=clasmodel.objects.all()
    return render(request=request,template_name="classes.html",context={"tabel":tabel})
###################################################################

#######################################################################
def index(request):
    tabel=clasmodel.objects.all()
    tabelp = personel.objects.all()
    tabel1=contactus.objects.all()
    return render(request=request, template_name="index.html",context={"tabel":tabel,"tabelp":tabelp,"tabel1":tabel1})
#######################################################################
def logink(request):
    form=login_form()
    return render(request=request, template_name="login.html",context={"form":form})
def registration(request):
    form=singup_form()
    return render(request=request, template_name="registration.html",context={"form":form})
def registrationp(request):
    form=singup_formp()
    return render(request=request, template_name="registrationp.html",context={"form":form})
#################################################################################
def teacher_single(request):
    user_st = userauth().state_and_login(request)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفتی
        per = personel.objects.filter(user_id=user_st["user"].id).all()

        return render(request=request, template_name="teacher-single.html",
                      context={"user_st": user_st, "per": per})
    else:
        return HttpResponse("وارد نشده 403 ")
def teacher(request):
    tabelp = personel.objects.all()
    form=teacher_form()
    return render(request=request, template_name="teacher.html", context={"tabelp": tabelp, "form": form})
def teacher_formm(request):
      form=teacher_form()
      return render(request=request, template_name="teacher_form.html",context={"form":form}) 
def loginp(requests):
    form = loginformp()
    return render(request=requests, template_name="loginp.html", context={"form": form})
def sabtp(request):
    if request.method == "POST":
        forms= teacher_form(request.POST,request.FILES)
        if forms.is_valid():
            user_st = userauth().state_and_login(request)
            us = personel(
                    name=forms.data["name"],
                    family = forms.data["family"],
                    cod_meli = forms.data["cod_meli"],
                    mahal_tavalod = forms.data["mahal_tavalod"],
                    datetime =forms.data["datetime"],
                    mizantahsilat= forms.data["mizantahsilat"],
                    reshtetahsili= forms.data["reshtetahsili"],
                    doreamozeshi= forms.data["doreamozeshi"],
                    sabeghekar = forms.data["sabeghekar"],
                    savabeghshoghli = forms.data["savabeghshoghli"],
                    semat = forms.data["semat"],                                
                    elattarkkar = forms.data["elattarkkar"],                             
                    semataknon = forms.data["semataknon"],
                    tahol = forms.data["tahol"],
                    namehamsar = forms.data["namehamsar"],
                    tedadfarzand= forms.data["tedadfarzand"],
                    tel= forms.data["tel"],                           
                    telsabet = forms.data["telsabet"],
                    adress_m = forms.data["adress_m"],
                    imagp = request.FILES['imagp'],
                    user_id = user_st["user"].id
            )
            us.save()
            return HttpResponseRedirect("/loginp")
        else:
     
                  
            id = forms.data["id"]
            result = personel.objects.filter(id=id).first()
            result.name=forms.data["name"],
            result.family = forms.data["family"],
            result.cod_meli = forms.data["cod_meli"],
            result.mahal_tavalod = forms.data["mahal_tavalod"],
            result.datetime =forms.data["datetime"],
            result.mizantahsilat= forms.data["mizantahsilat"],
            result.reshtetahsili= forms.data["reshtetahsili"],
            result.doreamozeshi= forms.data["doreamozeshi"],
            result.sabeghekar = forms.data["sabeghekar"],
            result.savabeghshoghli = forms.data["savabeghshoghli"],
            result.semat = forms.data["semat"],                                
            result.elattarkkar = forms.data["elattarkkar"],                             
            result.semataknon = forms.data["semataknon"],
            result.tahol = forms.data["tahol"],
            result.namehamsar = forms.data["namehamsar"],
            result.tedadfarzand= forms.data["tedadfarzand"],
            result.tel= forms.data["tel"],                           
            result.telsabet = forms.data["telsabet"],
            result.adress_m = forms.data["adress_m"],
            result.imagp = request.FILES['imagp'],
            
            result.save()
            return HttpResponse("true")

    else:
        return HttpResponse("false")
def deletk(request):
    if request.method == "POST":
        id = request.POST.get("id")
        user.objects.filter(id=id).delete()
        return HttpResponse("/true")
    else:
        return HttpResponse("false")
def deletpersonel(request):
    if request.method == "POST":
        id = request.POST.get("id")
        personel.objects.filter(id=id).delete()
        return HttpResponse("/true")
    else:
        return HttpResponse("false")
def cheklogins(request):  # چ کردن عملیات لاگین که ایا این کاربر قبلا ثبت نام کرده

    formsy = login_form(request.POST)
    if formsy.is_valid():
        user = authenticate(request, username=formsy.data["username"], password=formsy.data["password"])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/teacher_formm")
        else:
            return HttpResponse("کاربری با این مشخصات یافت نشد ")



def getp(request, pk):
    datap = get_object_or_404(personel.objects.select_related('user'), id=pk)

    return render(request=request, template_name="teacher-single.html", context={"datap": datap})   
#######################################################################################
def kodak_formm(request):
      form=kodak_form()
      return render(request=request, template_name="kodak_form.html",context={"form":form}) 
def panel(request):
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفتی
        clas= koodak.objects.filter(user_id=user_st["user"].id).all()
        return render(request=request, template_name="panelkoodak.html",
               context={"user_st": user_st,"clas":clas})
    else:
          return HttpResponse("وارد نشده 403 ")
def sabt(request):
    if request.method == "POST":
        formsy = kodak_form(request.POST,request.FILES)
        print(formsy)
        if formsy.is_valid():
            user_st = userauth().state_and_login(request)
            us = koodak(
                    name=formsy.data["name"],
                    family=formsy.data["family"],
                    cod_meli=formsy.data["cod_meli"],
                    mahal_tavalod=formsy.data["mahal_tavalod"],
                    datetime=formsy.data["datetime"],
                    namepedar=formsy.data["namepedar"],
                    tahsilatpedar=formsy.data["tahsilatpedar"],
                    shoghlepedar=formsy.data["shoghlepedar"],
                    telpedar=formsy.data["telpedar"],
                    adress_p=formsy.data["adress_p"],
                    namemadar=formsy.data["namemadar"],
                    tahsilatmadar=formsy.data["tahsilatmadar"],
                    shoghlmadar=formsy.data["shoghlmadar"],
                    telmadar=formsy.data["telmadar"],
                    telsabet=formsy.data["telsabet"],
                    adress_m=formsy.data["adress_m"],
                    adressmanzel=formsy.data["adressmanzel"],
                    codeposti=formsy.data["codeposti"],
                    vatsap=formsy.data["vatsap"],
                    imagk=request.FILES['imagk'],
                    user_id=user_st["user"].id  )
            us.save()
            return HttpResponseRedirect("/logink")
        else:
            id = formsy.data["id"]
            result = koodak.objects.filter(id=id).first()
            result.name = formsy.data["name"],
            result.family = formsy.data["family"],
            result.cod_meli = formsy.data["cod_meli"],
            result.mahal_tavalod = formsy.data["mahal_tavalod"],
            result.datetime = formsy.data["datetime"],
            result.namepedar = formsy.data["namepedar"],
            result.tahsilatpedar = formsy.data["tahsilatpedar"],
            result.shoghlepedar = formsy.data["shoghlepedar"],
            result.telpedar = formsy.data["telpedar"],
            result.adress_p = formsy.data["adress_p"],
            result.namemadar = formsy.data["namemadar"],
            result.tahsilatmadar = formsy.data["tahsilatmadar"],
            result.shoghlmadar = formsy.data["shoghlmadar"],
            result.telmadar = formsy.data["telmadar"],
            result.telsabet = formsy.data["telsabet"],
            result.adress_m = formsy.data["adress_m"],
            result.adressmanzel = formsy.data["adressmanzel"],
            result.codeposti = formsy.data["codeposti"],
            result.vatsap = formsy.data["vatsap"],
            result.imagk = request.FILES['imagk'],
            result.save()
            return HttpResponse("true")

    else:
        return HttpResponse("خطا")
def listk(requests):

    tabel = koodak.objects.all()
    form=kodak_form()  # این را به دلیل این اینجا نوشتیم که فرم داخل مدال بیاد
    return render(request=requests, template_name="koodakan.html", context={"tabel": tabel, "form": form})
def cheklogin(request):  # چ کردن عملیات لاگین که ایا این کاربر قبلا ثبت نام کرده

    formsy = login_form(request.POST)
    if formsy.is_valid():
        user = authenticate(request, username=formsy.data["username"], password=formsy.data["password"])
        if user is not None:
            login(request, user)

            return HttpResponseRedirect("/kodak_formm")
        else:
            return HttpResponse("کاربری با این مشخصات یافت نشد ")
            #return render(request,"login.html")
def sing_up1(request):
    if request.method == "POST":
        formsy = singup_form(request.POST)
        if formsy.is_valid():
            userss = User.objects.filter(username=formsy.data["username"]).all()
            if len(userss) > 0:
                return HttpResponse("قبلا وجود دارد")
            else:
                us = User.objects.create_user(username=formsy.data["username"], password=formsy.data["password"],
                                              email=formsy.data["username"])
                us.firstname = formsy.data["name"]
                us.lastname = formsy.data["family"]
                us.save()
                return HttpResponseRedirect("/logink")
        else:
            return HttpResponse("انجام نشد")
def sing_upp(request):
    if request.method == "POST":
        formsy = singup_formp(request.POST)
        if formsy.is_valid():
            userss = User.objects.filter(username=formsy.data["username"]).all()
            if len(userss) > 0:
                return HttpResponse("قبلا وجود دارد")
            else:
                us = User.objects.create_user(username=formsy.data["username"], password=formsy.data["password"],
                                              email=formsy.data["username"])
                us.firstname = formsy.data["name"]
                us.lastname = formsy.data["family"]
                us.save()
                return HttpResponseRedirect("/loginp")
        else:
            return HttpResponse("انجام نشد")        
def chekout(request):
    if request.user.is_authenticated:  # کاربر لاگین شده یا نه
        return HttpResponse("وارد شده")
    else:
        return HttpResponse("وارد نشده ")
def logouts(request):
    logout(request)
    return HttpResponseRedirect("/index")
def get(request,pk):
        data= get_object_or_404(koodak.objects.select_related('user'), id=pk)
        return render(request=request, template_name="panelkoodak.html", context={"data": data})   
#####################################################################################
def contact(request):
    form=contactusmodel()
    return render(request=request, template_name="contact.html",context={"form":form})
def readallask(request):
    if request.method=="POST":
         if str(request.POST.get("tocken"))=="bvnbvnvnb":#مقدار توکن رو بررسی میکن
             user_st = userauth().state_and_login(request) #ایا کاربر لاگین شده
             if  user_st["state"]:#اگه شده
                 search= request.POST.get("search")
                 listdata = ask.objects.filter(user_id=user_st["user"].id).all()
                 if search=="":#اگه مقدار سرچش خال بود
                     listdata = ask.objects.filter(user_id=user_st["user"].id , title=search).all()



                 myserdata = serializers.serialize("json", listdata)
                 return HttpResponse(myserdata)


    return HttpResponse("403")
def contact(request):  # 255
    # msg=""
    action = "/contact"  # برای ویرایش
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    print(ip_adress)
    if request.method == "POST":
        forms = contactusmodel(request.POST)

        if forms.is_valid():
            result = contactus(namefull=forms.data["namefull"], email=forms.data["email"], ip=ip_adress,
                               masg=forms.data["masg"])
            result.save()
            # msg=" عزیز " +form.data["namefull"]+ "ممنون از "
            return HttpResponseRedirect(
                "/mycomment")  # برای این است که وقتی فرم روپر کردیم و ارسال رو زدیم دوباره فرم خالی میشه
        else:
            # msg="دیتا معتبر نیس"
            return render(request=request, template_name="contact.html", context={"form": forms})

    forms = contactusmodel()
    return render(request=request, template_name="contact.html", context={"form": forms, "action": action})
def savecontact(request):  # دریافت اطلاعات ارسالی از کاربر در ویو و برگشت به کس دیگه

    if request.method == "POST":
        form = contactusmodel(request.POST)
        return HttpResponse(+form.data["namefull"] + "ممنون")
def mycomment(request):  # بعد از زدن ارسال این تابع اجرا میشه
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    listcomment = contactus.objects.filter(ip=ip_adress).all()
    forms = contactusmodel()
    return render(request=request, template_name="index.html", context={"list": listcomment, "form": forms})
def edit(request, id):  # برای ویرایش
    result = contactus.objects.filter(id=id).first()
    action = "/editsave"
    forms = contactusmodel(initial={"id": id, "namefull": result.namefull, "email": result.email, "masg": result.masg})
    return render(request=request, template_name="contact.html", context={"forms": forms, "action": action})
def editsave(request):  # برای ویرایش
    if request.method == "POST":
        forms = contactusmodel(request.POST)
        id = forms.data["id"]
        result = contactus.objects.filter(id=id).first()
        result.namefull = forms.data["namefull"]
        result.email = forms.data["email"]
        result.masg = forms.data["masg"]
        result.save()
        return HttpResponseRedirect("/mycomment")
def delete(request, id):  # برای حذف
    result = contactus.objects.filter(id=id).first()
    result.delete()
    return HttpResponseRedirect("/mycomment")
#########################################################################################
def faqs(request):
    dataask = ask.objects.all()
    panelask=askform()
    return render(request=request, template_name="faqs.html",context={"panelask":panelask,"dataask":dataask,})
def panelask(request):
    
      panelask = askform()
      return render(request=request, template_name="faqs.html",
                      context={ "panelask": panelask})
def getmyask(request):
    user_st = userauth().state_and_login(request)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفتی
        print(user_st["user"].id)
        listmyask = ask.objects.filter(user_id=user_st["user"].id).all()
        for item in listmyask:
            print(item.title)
        return HttpResponse(str(listmyask))
    else:
        return HttpResponse("عدم دسترسی")
def deletask(request):
    if request.method == "POST":
        id = request.POST.get("id")
        ask.objects.filter(id=id).delete()
        return HttpResponse("/true")
    else:
        return HttpResponse("false")
def saveasks(request):
       if request.method=="POST":
             forms=askform(request.POST)

             if forms.is_valid():
                user_st= userauth().state_and_login(request)
                id=forms.data["id"]
                if id=="0":
                   datast=ask.objects.filter(title=forms.data["title"]).all()
                   if len(datast)>0:
                    return HttpResponse("exit")
                   x=datetime.datetime.now()
                   newask=ask(title=forms.data["title"],caption=forms.data["caption"],
                              created=x,user_id= user_st["user"].id )

                   newask.save()
                   return HttpResponse("true")
                else:
                    editask=ask.objects.filter(id=id).first()
                    editask.title=forms.data["title"]
                    editask.caption=forms.data["caption"]
                    editask.save()
                    return HttpResponse("true")
             else:
              return HttpResponse("valid")
       else:
              return HttpResponse("false")
def commentasks(request):
    commentasks=commentaskform()
    return render(request=request,template_name="faqs.html",context={"commentasks":commentasks})
def listask(request):
    dataask = ask.objects.all()
    listask = askform()
    commentasks=commentaskform()
    return render(request=request, template_name="faqs.html",
                  context={"listask": listask, "dataask": dataask, "commentasks":commentasks})
def savejavab(request):
    if request.method == "POST":
        formj = commentaskform(request.POST)

        if formj.is_valid():
            user_st = userauth().state_and_login(request)

            x = datetime.datetime.now()
            newask = commentask(text=formj.data["text"],created=x,ask_id=formj.data["ask_id"],user_id=user_st["user"].id)
            newask.save()
            return HttpResponse("true")

        else:
            return HttpResponse("false")
def get_ask_with_comment(request,pk):
    print(pk)
    askis= get_object_or_404(commentask.objects.select_related('ask'), id=pk)
    print(askis.text)

    return render(request=request, template_name="javab.html", context={"listmyjavab": askis})
def listask1(request):
    dataask = ask.objects.all()
    listask = askform()
    commentasks=commentaskform()
    return render(request=request, template_name="listask.html",
                  context={"listask": listask, "dataask": dataask, "commentasks":commentasks})
################################################################################  
def gallery_2(request):
        form=imageuploadform(request.POST,request.FILES)
        return render(request=request,template_name="upload_image.html",context={'form':form})    
def gallery_3(request):
    return render(request=request, template_name="gallery-3.html")
def gallery(request):
    return render(request=request, template_name="gallery.html")
def upload_image(request):
    if request.method == 'POST':
        form=imageuploadform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect("/upload_image")
        else:
            form=imageuploadform()
        return render(request=request,template_name="upload_image.html",context={'form':form})    
def show_image_all(request):
    images=imageModel.objects.all()
    return render(request=request,template_name="filtered_images.html",context={"images":images})   

def filtered_images(request,filter_choice):
    print(filter_choice)
    image=imageModel.objects.filter(filter_choice=filter_choice)
    print(image)
    return render(request=request,template_name="filter.html",context={"image":image})  

def film(request):
    filmm = films.objects.all()
    return render(request=request, template_name="gallery.html",context={"filmm":filmm})
def creatfilm(request):
    if request.method =="POST":
        film = filmform(request.POST,request.FILES)
        if film.is_valid():
          ff=films(name=film.cleaned_data['name'], film=request.FILES['film'])

          ff .save()
        else:
            film = filmform()
            return render(request=request, template_name="creatfilm.html", context={"film": film})
    film = filmform()
    return render(request=request, template_name="creatfilm.html", context={"film": film})

  

def creatveblogmorabi(request):
      form=veblogp_form()
      return render(request=request, template_name="creatveblogmorabi.html",context={"form":form})  
def listveblogmorabi(request):
    imgp=veblogp.objects.all()
    return render(request=request,template_name="gallery-3.html",context={"imgp":imgp})

   
#######################################################
def setsession(request):
    request.session["name"]="vahideh"
    return HttpResponseRedirect("getsession")
def getsession(request):
    del request.session["name"]
    return HttpResponse(request.session.get("name"))
def setcookis(request):
    repoz=HttpResponse()
    repoz.set_cookie("username","vahideh")
    return repoz
def getcookis(request):
   return HttpResponse(request.COOKES["username"])

