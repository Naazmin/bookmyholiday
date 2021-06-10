from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userlogindata(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.user.username

class destinations(models.Model):
    dname = models.CharField(max_length=60)
    def __str__(self):
        return self.dname

class vehicletype(models.Model):
    vname = models.CharField(max_length=60)
    def __str__(self):
        return self.vname

class package(models.Model):
    pname = models.CharField(max_length=60)
    pdesc = models.CharField(max_length=255)
    pdestination = models.ForeignKey(destinations, on_delete=models.DO_NOTHING) 
    paccomudation = models.CharField(max_length=255)
    price = models.IntegerField()
    days = models.IntegerField(null=True, blank=True)
    pimg = models.ImageField(null=True, blank=True,upload_to='pkgimg/')
    pimg1 = models.ImageField(null=True, blank=True,upload_to='pkgimg/')
    pimg2 = models.ImageField(null=True, blank=True,upload_to='pkgimg/')

    ratings = models.IntegerField(default=0)
    def __str__(self):
        return self.pname
class comment(models.Model):
    user = models.ForeignKey(userlogindata, on_delete=models.DO_NOTHING)
    coment = models.CharField(max_length=255)
    cratings = models.IntegerField()
    pakage = models.ForeignKey(package, on_delete=models.DO_NOTHING) 

class Enquery(models.Model):
    user = models.ForeignKey(userlogindata, on_delete=models.DO_NOTHING)
    enquerys = models.CharField(max_length=255)
    reply = models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField(default=False,null=True, blank=True)
    startdate = models.DateField(auto_now=False, auto_now_add=True)

class vehicle(models.Model):
    name = models.CharField(max_length=60)
    destination = models.ForeignKey(destinations, on_delete=models.DO_NOTHING) 
    vtype = models.CharField(max_length=50)
    seats = models.IntegerField()
    pak = models.ForeignKey(package,on_delete=models.DO_NOTHING,null=True)
    vprice = models.IntegerField()
    vimg = models.ImageField(null=True, blank=True,upload_to='vehicleimg/')
    mtype = models.ForeignKey(vehicletype, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name 

class hotels(models.Model):
    hotelname = models.CharField(max_length=60)
    loaction = models.ForeignKey(destinations, on_delete=models.DO_NOTHING) 
    ratings = models.IntegerField()
    price = models.IntegerField()
    himg = models.ImageField(null=True, blank=True,upload_to='hotelimg/')
    def __str__(self):
        return self.hotelname


class mybookings(models.Model):
    user = models.ForeignKey(userlogindata, on_delete=models.DO_NOTHING)
    pakage = models.ForeignKey(package, on_delete=models.DO_NOTHING) 
    mvehicle = models.ForeignKey(vehicle, on_delete=models.DO_NOTHING,blank=True ,null=True) 
    mhotle = models.ForeignKey(hotels, on_delete=models.DO_NOTHING,blank=True,null=True) 
    members = models.IntegerField()
    source = models.CharField(max_length=60)
    fromdate = models.DateField()
    #todate = models.DateField()
    status = models.BooleanField(default=False)




