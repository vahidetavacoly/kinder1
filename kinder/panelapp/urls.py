from django.urls import path, re_path


from . import views
urlpatterns = [

   
    path('about', views.about,name="درباره ما  "),
    path('blog_classic', views.blog_classic,name="وبلاگ کلاسیک   "),
    path('blog_grid', views.blog_grid,name="وبلاگ   "),
    path('blog_single', views.blog_single,name="وبلاگ مجرد   "),
   
    path('class_schedule', views.class_schedule,name="  برنامه ها  "),
    path('class_single', views.class_single,name=" کلاس جزییات    "),
    path('class', views.classes,name="  لیست کلاس فوق برنامه   "),
   
    path('contact', views.contact,name=" تماس با ما   "),
  
  
   
    path('faqs', views.faqs,name="   سوالات "),
    path('gallery_2', views.gallery_2,name=" تصاویر 2   "),
    path('gallery_3', views.gallery_3,name="تصاویر 3    "),
    path('gallery', views.gallery,name=" تصاویر  "),
  
    path('index', views.index,name="صفحه اصلی   "),
    path('logink', views.logink,name="ورود   "),
   
    path('registration', views.registration,name=" برای لاگین ثبت نام    "),
    path('registrationp', views.registrationp,name=" برای لاگین ثبت نام    "),
       
    path('teacher_single', views.teacher_single,name="پنل مربی   "), 
    path('teacher', views.teacher,name="لیست مربیان    "),
    ############################################################
    path('teacher_formm', views.teacher_formm,name="فرم ثبت نام مربی    "), 
    path('kodak_formm', views.kodak_formm,name="فرم ثبت نام کودک    "), 
   
    path('sing_upp', views.sing_upp,name="عضو شدن در سایت     "),

    path('cheklogin', views.cheklogin,name="  چک کردن عملیات لاگین  "), 
    path('chekout', views.chekout,name="   ایا لاگین شده یا نه   "), 
    path('logouts', views.logouts,name="    خارج شدن از حساب کاربری    "),
    path('panel', views.panel,name="پنل کودک "),
    path('sabt', views. sabt, name="ثبت نام   "),
    path('listk', views.listk, name="لیست نواموزان"),
    #از این قسمت به پایین مربوط به پرسنل میشود
   
    path('sabtp', views.sabtp, name="ثبت نام پرسنل  "),
    path('getp/<int:pk>', views.getp, name="  "),
    path('get/<int:pk>', views.get, name="  "),
    path('cheklogins', views.cheklogins, name="چک کردن ورود پرسنل "),
    path('loginp', views.loginp, name="صفحه ورود پرسنل"),
   
    path('deletk', views.deletk, name="حذف کودک "),
    path('deletpersonel', views.deletpersonel, name="حذف پرسنل"),
    ##############################################################################
    path('mycomment', views.mycomment, name=" لیست نظرات  "),
    path('edit/<int:id>', views.edit, name=" ویرایش "),#برای ویرایش
    path('editsave', views.editsave, name=" ذخیره ویرایش "),#برای ویرایش
    path('delete/<int:id>', views.delete, name=" حذف "),#برای حذف
    path('panelask', views.panelask, name="پنل سوال"),
    path('getmyask', views.getmyask, name=" گرفتن سوال"),
    path('saveasks', views.saveasks, name="ذخیره سوال"),
    path('listask', views.listask, name=" گرفتن سوال"),
    path('commentasks', views.commentasks, name="ذخیره سوال"),
    path('deletask', views.deletask, name="حذف سوال"),
    path('savejavab', views.savejavab, name="ذخیره جواب "),
    path('readallask', views.readallask, name="حذف اطلاعات"),
    path('get_ask_with_comment/<int:pk>', views.get_ask_with_comment, name="  "),
    ###################################################################
 
  
    path('film', views.film, name=""),
    path('creatfilm', views.creatfilm, name=" "),
   
   
    path('saveclas', views.saveclas, name=" "),
    
    path('saveveblog', views.saveveblog, name=" "),
    path('creatclas', views.creatclas, name="بارگذاری کلاس ها  "),
    path('creatveblog', views.creatveblog, name=" بارکذاری پست ها "),
    path('creatveblogmorabi', views.creatveblogmorabi, name="بارگذاری   وبلاگ مربی  "),
    path('listask1', views.listask1, name="        جواب دادن به سوالات  "),
  
    ###################################################################
    path('upload_image', views.upload_image, name="اپلود عکس" ),
    path('show_image_all', views.show_image_all, name="  "),
    path('filter/<str:filter_choice>', views.filtered_images, name="  "),
    
  
    path(' setsession', views.setsession, name="  "),
    path('getsession', views.getsession, name="    "),
    path('setcookis', views.setcookis, name=" "),
    path('getcookis', views.getcookis, name="    "),
  
    

    ]


    




