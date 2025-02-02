from django import forms
from django_jalali.forms import jDateField,jDateTimeField
from django_jalali.admin.widgets import AdminjDateWidget,AdminSplitjDateTime
from .models import imageModel

class singup_form(forms.Form):
    def __init__(self,*args,**kwargs):
        super(singup_form,self).__init__(*args,**kwargs)
        for item in singup_form.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"

    name = forms.CharField(required=True, label="نام  ", )
    family = forms.CharField(required=True, label="نام خانوادگی ")
    username=forms.CharField(required=True,label="نام کاربری ",)
    password=forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput)
class singup_formp(forms.Form):
    def __init__(self,*args,**kwargs):
        super(singup_formp,self).__init__(*args,**kwargs)
        for item in singup_formp.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"

    name = forms.CharField(required=True, label="نام  ", )
    family = forms.CharField(required=True, label="نام خانوادگی ")
    username=forms.CharField(required=True,label="نام کاربری ",)
    password=forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput)    
class kodak_form(forms.Form):
    name = forms.CharField(required=True,label="نام ",widget=forms.TextInput(attrs={'class':'form-control'}))
    family = forms.CharField(required=True,label="نام خانوادگی",widget=forms.TextInput(attrs={'class':'form-control'}))
    cod_meli = forms.IntegerField(required=True,label="کد ملی/ش.شناسنامه",widget=forms.TextInput(attrs={'class':'form-control'}))
    mahal_tavalod = forms.CharField(required=True,label="محل تولد",widget=forms.TextInput(attrs={'class':'form-control'}))
    datetime = jDateField(widget=AdminjDateWidget(),label="تاریخ تولد")
    namepedar = forms.CharField(required=True, label="نام پدر", widget=forms.TextInput(attrs={'class': 'form-control'}))
   
    tahsilatpedar = forms.CharField(required=True, label="میزان تحصیلات پدر",
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    shoghlepedar = forms.CharField(required=True, label="شغل پدر",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    telpedar = forms.IntegerField(required=True, label="همراه پدر",
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    adress_p = forms.CharField(required=True, label="ادرس محل کار پدر",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    namemadar = forms.CharField(required=True, label="نام مادر",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
   
    tahsilatmadar = forms.CharField(required=True, label="تحصیلات مادر",
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    shoghlmadar = forms.CharField(required=True, label="شغل مادر",
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    telmadar = forms.IntegerField(required=True, label="همراه مادر",
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    telsabet = forms.CharField(required=True, label="تلفن ثابت",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    adress_m = forms.CharField(required=True, label="ادرس محل کار مادر",  widget=forms.TextInput(attrs={'class': 'form-control'}))

    adressmanzel = forms.CharField(required=True, label="ادرس محل سکونت",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    codeposti = forms.IntegerField(required=True, label="کد پستی",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    vatsap = forms.IntegerField(required=True, label="واتساپ", widget=forms.TextInput(attrs={'class': 'form-control'}))
    imagk = forms.ImageField(required=False, label="عکس"  )
    id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")

class login_form(forms.Form):
    def __init__(self,*args,**kwargs):
        super(login_form,self).__init__(*args,**kwargs)
        for item in login_form.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"
    username=forms.CharField(required=True,label="نام کاربری ",)
    password=forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput)
class loginformp(forms.Form):
     def __init__(self,*args,**kwargs):
        super(loginformp,self).__init__(*args,**kwargs)
        for item in loginformp.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"
     username=forms.CharField(required=True,label="نام کاربری ",)
     password=forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput)    
class teacher_form(forms.Form):
     name = forms.CharField(required=True,label="نام ",widget=forms.TextInput(attrs={'class':'form-control'},))
     family = forms.CharField(required=True,label="نام خانوادگی",widget=forms.TextInput(attrs={'class':'form-control'}))
     cod_meli = forms.IntegerField(required=True,label="کد ملی/ش.شناسنامه",widget=forms.TextInput(attrs={'class':'form-control'}))
     mahal_tavalod = forms.CharField(required=True,label="محل تولد",widget=forms.TextInput(attrs={'class':'form-control'}))
     datetime = jDateField(widget=AdminjDateWidget(), label="تاریخ تولد")
     CHOICES = (('Option 1', 'دیپلم'),('Option 2', 'فوق دیپلم'),('Option 3', 'لیسانس'),('Option 4', 'فوق لیسانس'))
     mizantahsilat= forms.ChoiceField(choices=CHOICES,required=True, label="میزان تحصیلات", widget=forms.Select(attrs={'class': 'form-control'}))
     reshtetahsili= forms.CharField(required=True, label="رشته تحصیلی", widget=forms.TextInput(attrs={'class': 'form-control'}))
     doreamozeshi= forms.CharField(required=True, label="دوره های اموزشی",
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

     CHOICES =(('Option 1', '1'),('Option 2', '2'),('Option 3', '3'),('Option 4', '4'),('Option 5', '5'),('Option 6', '6'),('Option 7', '7'),('Option 8', '8'),('Option 9', '9'),('Option 10', '10'),('Option 11', '11'),('Option 12', '12'),('Option 13', '13'),('Option 14', '14'),('Option 15', '15'),('Option 16', '16'))
     sabeghekar = forms.ChoiceField(choices=CHOICES,required=True, label="سابقه کار", widget=forms.Select(attrs={'class': 'form-control'}))

     savabeghshoghli = forms.CharField(required=True, label="سوابق شغلی",
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
     semat = forms.CharField(required=True, label="سمت قبلی",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
     elattarkkar = forms.CharField(required=True, label="علت ترک کار",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
     semataknon = forms.CharField(required=True, label="سمت در این مجموعه",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

     CHOICES = (('Option 1', 'مجرد'), ('Option 2', 'متاهل'))
     tahol = forms.ChoiceField(required=True,choices=CHOICES, label="وضعیت تاهل",
                                widget=forms.Select(attrs={'class': 'form-control'}))
     namehamsar = forms.CharField(required=True, label="نام همسر",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
     CHOICES = (('Option 1', '1'), ('Option 2', '2'), ('Option 3', '3'), ('Option 4', '4'), ('Option 5', '5'))
     tedadfarzand= forms.ChoiceField(required=True,choices=CHOICES, label="تعداد فرزند",
                               widget=forms.Select(attrs={'class': 'form-control'}))


     tel= forms.IntegerField(required=True, label="همراه",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
     telsabet = forms.IntegerField(required=True, label="تلفن ثابت", widget=forms.TextInput(attrs={'class': 'form-control'}))

     adress_m = forms.CharField(required=True, label="ادرس محل سکونت",
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
     imagp = forms.ImageField(required=False, label="عکس" )
     id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")
   
class filmform(forms.Form):
    def __init__(self, *args, **kwargs):
        super(filmform, self).__init__(*args, **kwargs)
        for item in filmform.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    name=forms.CharField(max_length=200)
    film=forms.FileField()               
class contactusmodel(forms.Form):
    def __init__(self,*args,**kwargs):
        super(contactusmodel,self).__init__(*args,**kwargs)
        for item in contactusmodel.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"
    namefull=forms.CharField(required=True,label="نام کامل")
    email=forms.EmailField(required=True,label="ایمیل")

    masg = forms.CharField(required=True, label="پیام ")
    id= forms.CharField(widget=forms.HiddenInput,required=True,initial="0",label="")
class askform(forms.Form):
    def __init__(self,*args,**kwargs):
        super(askform,self).__init__(*args,**kwargs)
        for item in askform.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"
    title=forms.CharField(required=True,label="عنوان سوال  ")
    caption=forms.CharField(required=True,label="متن سوال ",widget=forms.Textarea())

    id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")
class commentaskform(forms.Form):
    def __init__(self, *args, **kwargs):
        super(commentaskform, self).__init__(*args, **kwargs)
        for item in commentaskform.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"
    #ask_id=forms.CharField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")در ویس بهتون میگم ممنونم
    text = forms.CharField(required=True, label="پاسخ سوال  ", widget=forms.Textarea())

    id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(), initial="0")
class clas_form(forms.Form):
    
   
    nameclas=forms.CharField(required=True,label=" نام کلاس",widget=forms.TextInput(attrs={'class':'form-control'},))
    namemorabi=forms.CharField(required=True,label=" نام مربی",widget=forms.TextInput(attrs={'class':'form-control'},))
    roz = forms.CharField(required=True,label=" روزهای کلاس",widget=forms.TextInput(attrs={'class':'form-control'},))
    time = jDateTimeField(widget=AdminSplitjDateTime(),label="  ساعت کلاس " )
    age= forms.IntegerField(required=True,label=" رده سنی",widget=forms.TextInput(attrs={'class':'form-control'},))
    price= forms.IntegerField(required=True,label=" شهریه",widget=forms.TextInput(attrs={'class':'form-control'},))
    tedad_jalasat=forms.CharField(required=True,label=" تعداد جلسات",widget=forms.TextInput(attrs={'class':'form-control'},))
    datetime=jDateField(widget=AdminjDateWidget(),label=" تاریخ شروع")
class veblog_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super(veblog_form, self).__init__(*args, **kwargs)
        for item in veblog_form.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"
    
    title=forms.CharField(required=True)
    post=forms.CharField(required=True)

class veblogp_form(forms.Form):
    def __init__(self,*args,**kwargs):
        super(veblogp_form,self).__init__(*args,**kwargs)
        for item in veblogp_form.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"
    title=forms.CharField(required=True,label="عنوان سوال  ")
    post=forms.CharField(required=True,label="متن سوال ",widget=forms.Textarea())
    #clasmodel=forms.CharField(required=True, label="نام کلاس ", widget=forms.HiddenInput(),initial="0")
    #personel=forms.CharField(required=True, label=" سمت", widget=forms.HiddenInput(),initial="0")
    id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")        
class imgvarzesh_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super(imgvarzesh_form, self).__init__(*args, **kwargs)
        for item in imgvarzesh_form.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"
    name=forms.CharField(required=True)
    imgmah=forms.ImageField(required=False, label="عکس") 

#############################################    
class imageuploadform (forms.ModelForm):
    class Meta:
        model = imageModel
        fields = ['image','filter_choice']
        CHOICES =(('Option1','pish1'),('Option2 ','pish2'),('Option3 ','naghashi '),('Option4 ','varzesh '),('Option5 ','morabi '),('Option6 ','koodak '),('Option7 ','mahd '))
        widgets ={'filter_choice':forms.Select(choices=CHOICES)}
  
               