from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('',homepageview,name = "homepage"),
    path('logout/',logoutuser,name = "logout"),
    path('user/login/',userloginpage,name = "userloginpage"),
    path('user/login/validate/',userlogin,name = "userlogin"),
    path('user/homepage/',userhomepage,name = "userhomepage"),
    path('packagedetails/<int:taskid>/',packagedetails,name = "packagedetails"),
    path('vehicleselection/<int:taskid>/',vehicleselection,name = "vehicleselection"),
    path("hotles/<int:mybookingid>/<int:vehicleid>/",hotles, name="hotles"),
    path('addcoment/<int:taskid>/',addcoment, name = "addcoment"),
    path("summary/<int:mybookingid>/<int:hotelid>/",summary, name="summary"),
    path("admin1/",adminpage,name='adminpage'),
    path("adminpackage/",adminpackage,name='adminpackage'),
    path("adminvehicle/",adminvehicle,name='adminvehicle'),
    path("adminhotel/",adminhotel,name='adminhotel'),
    path('register/',register,name='register'),

    path("bookings/",adminbookings,name='bookings'),

    path('adddest/',adddest,name = "adddest"),
    path('booksucess/<int:taskid>/',booksucess, name = "booksucess"),
    path('mybooking1/',mybooking1,name = "mybooking1"),
    path('myenquiry/',myenquiry,name = "myenquiry"),
    path('adminenquiry/',adminenquiry,name = "adminenquiry"),
    path("editvehicle/<int:taskid>/<int:mybookingid>/",editvehicle, name="editvehicle"),

    path('tour/',tour,name = "tour"),
    path('addquery/',addquery,name = "addquery"),
    path('replyquery/<int:taskid>/',replyquery, name = "replyquery"),



   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   
