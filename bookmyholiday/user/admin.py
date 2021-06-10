from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([
    userlogindata,
    vehicle,
    comment,
    package,
    Enquery,
    mybookings,
    destinations,
    vehicletype,
    hotels
    

   


   
])