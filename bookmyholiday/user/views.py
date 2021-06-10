from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.dateparse import parse_datetime
from .models import *
from .forms import *
from datetime import timedelta
from .decorators import *
def homepageview(request):
    packages=package.objects.all()
    context = {'packages' : packages}
    return render(request, "user/homepage.html",context)

def userloginpage(request):
    return render(request,"user/userloginpage.html")

def userlogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,'username or password is in correct')
			
    return redirect(request.META["HTTP_REFERER"])
@login_required(login_url='userloginpage')
def userhomepage(request):
    if request.user.is_superuser:
        messages.add_message(request,messages.INFO,"you must login as user")
        logout(request)
        return redirect("userloginpage")
    workunits = ["My feedbacks"]
    context = {'workunits' : workunits,'username' : request.user.username}
    return render(request,"user/userhomepage.html",context)

def logoutuser(request):
    logout(request)
    return redirect("homepage")

def register(request):
	form=CreateUserForm()
	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			group=Group.objects.get(name='user')
			user.groups.add(group)
			userlogindata.objects.create(
               user=user,
				)
			messages.success(request,'Account is created')
			return redirect('userloginpage')

	return render(request,'user/register.html',{'form':form})

def packagedetails(request,taskid):
    pdata = package.objects.get(id=taskid)
    pcoments = comment.objects.filter(pakage=pdata)
    context = {'package' : pdata,"coments":pcoments,"pkgid":pdata.id}
    return render(request,"user/packagedetails.html",context)

@login_required(login_url='userloginpage')
def vehicleselection(request,taskid):
    source = request.POST['source']
    members = request.POST['members']
    fromdate = request.POST['fromdate']
    print(fromdate)
    #todate= timedelta(days=vehicle.objects.get(id=taskid).pak.days) + parse_datetime(fromdate) 
    #print(todate)
    pdata = package.objects.get(id=taskid)
    mbus = vehicletype.objects.get(vname='bus')
    mcar = vehicletype.objects.get(vname='car')
    print(request.user)
    user1 = userlogindata.objects.get(user=request.user)
    books = mybookings(user=user1,pakage=pdata,members=members,source=source,fromdate=fromdate)
    books.save()
    bus1 = vehicle.objects.filter(destination=pdata.pdestination).filter(mtype=mbus)
    car1 = vehicle.objects.filter(destination=pdata.pdestination).filter(mtype=mcar)
    print(books)
    context = {'mybooking' : books,"buss":bus1,"cars":car1}
    return render(request,"user/vehicalselection.html",context)
@login_required(login_url='userloginpage')
def hotles(request,mybookingid,vehicleid):
    print(mybookingid)
    print(vehicleid)
    mybookingss = mybookings.objects.get(id=mybookingid)
    veh = vehicle.objects.get(id=vehicleid)
    mybookingss.mvehicle=veh
    mybookingss.save()
    print(mybookingss.pakage.pdestination)
    hotelss = hotels.objects.filter(loaction=mybookingss.pakage.pdestination)
    context = {'mybooking' : mybookingss,"hotels":hotelss,"mybookingid":mybookingid}
    print(veh)
    print(hotelss)
    print(mybookingss)
    return render(request,"user/hotelselection.html",context)

@login_required(login_url='userloginpage')
def addcoment(request,taskid):
    comment1 = request.POST['comment']
    ratings = request.POST['rating']
    pdata = package.objects.get(id=taskid)
    user1 = userlogindata.objects.get(user=request.user)
    print(comment)
    print(ratings)
    print(pdata)
    print(user1)
    comentss = comment(user=user1,coment=comment1,cratings=ratings,pakage=pdata)
    comentss.save()
    return redirect('packagedetails', taskid=taskid)


@login_required(login_url='userloginpage')
def summary(request,mybookingid,hotelid):
    mybookingss = mybookings.objects.get(id=mybookingid)
    #from1 = mybookings.objects.get(id=mybookingid).fromdate
    #to1 = mybookings.objects.get(id=mybookingid).todate
    #dat=to1-from1
   # a = float(str(dat)[0])
    a = mybookings.objects.get(id=mybookingid).pakage.days
    htl = hotels.objects.get(id=hotelid)
    mybookingss.mhotle=htl
    mybookingss.save()
    ppprice = mybookingss.pakage.price
    tvprice = mybookingss.mvehicle.vprice
    hhprice = mybookingss.mhotle.price
    membersss = mybookingss.members
    halfmem = membersss / 2
    halfmem = int(halfmem)
    thprice = halfmem * hhprice
    thprice=thprice*a

    mbus = vehicletype.objects.get(vname='bus')    
    mcar = vehicletype.objects.get(vname='car')                      
    if(mybookingss.mvehicle.mtype == mbus):
        tvprice = tvprice * membersss
    if(mybookingss.mvehicle.mtype == mcar):
        tvprice = tvprice * a
    tvprice = int(tvprice)
    totalprice = ppprice + thprice + tvprice
    totalprice = int(totalprice)
    tusd = int(totalprice/70)
   
    print(tusd)
    context = {'mybooking' : mybookingss,"mybookingid":mybookingid,"tvprice":tvprice,"thprice":thprice,"halfmem":halfmem,"tprice":totalprice,"tusd":tusd}
    return render(request,"user/ordersummary.html",context)
@login_required(login_url='userloginpage')
@allowed_users(allowed_roles=['adminn'])
def adminpage(request):
    return render(request,"admin/adminhome.html")
@login_required(login_url='userloginpage')
@allowed_users(allowed_roles=['adminn'])
def adminpackage(request):
    form=packageForm()
    if request.method=='POST':
        form=packageForm(request.POST,request.FILES)
        
        form.save()

    return render(request,"admin/adminpackage.html",{'form':form})   

@login_required(login_url='userloginpage') 
@allowed_users(allowed_roles=['adminn'])    
def adminvehicle(request):
    form=vehicleForm()
    if request.method=='POST':
        form=vehicleForm(request.POST,request.FILES)
        
        form.save()

    return render(request,"admin/asminvehicle.html",{'form':form}) 

@login_required(login_url='userloginpage') 
@allowed_users(allowed_roles=['adminn'])   
def adminhotel(request):
    form=hotelForm()
    if request.method=='POST':
        form=hotelForm(request.POST,request.FILES)
        
        form.save()

    return render(request,"admin/adminhotel.html",{'form':form})    


@login_required(login_url='userloginpage')
@allowed_users(allowed_roles=['adminn'])
def adminbookings(request):
    admin2=mybookings.objects.filter(status=True)
    return render(request,"admin/adminhistory.html",{'admin2':admin2})     



def adddest(request):
    dname11 = request.POST['dname1']
    dest=destinations(dname=dname11)
    dest.save()
    return render(request,"admin/adminhome.html")


def booksucess(request,taskid):
    mybookingss = mybookings.objects.get(id=taskid)
    myveh = mybookingss.mvehicle
    vehicl = vehicle.objects.get(name=myveh)
    mbus = vehicletype.objects.get(vname='bus')                       
    if(vehicl.mtype == mbus):
        steat1 = vehicl.seats
        mem = mybookingss.members
        rem = steat1-mem
        vehicl.seats=rem
        vehicl.save()
    mybookingss.status=True
    mybookingss.save()
    return redirect("homepage")



def mybooking1(request):
    user1 = userlogindata.objects.get(user=request.user)
    mybook1=mybookings.objects.filter(status=True).filter(user=user1)
    print(mybook1)
    context = {"mybook1":mybook1}
    return render(request,"user/mybookings1.html",context)

def myenquiry(request):
    user1 = userlogindata.objects.get(user=request.user)
    myenq = Enquery.objects.filter(user=user1)
    context = {"myenq":myenq}
    return render(request,"user/myenquiryy.html",context)

def adminenquiry(request):
    myenq = Enquery.objects.filter(status=False)
    context = {"myenq":myenq}
    return render(request,"admin/enqury.html",context)


def editvehicle(request,taskid,mybookingid):
    pdata = package.objects.get(id=taskid)
    mbus = vehicletype.objects.get(vname='bus')
    mcar = vehicletype.objects.get(vname='car')
    bus1 = vehicle.objects.filter(destination=pdata.pdestination).filter(mtype=mbus)
    car1 = vehicle.objects.filter(destination=pdata.pdestination).filter(mtype=mcar)
    context = {'mybooking' : mybookingid,"buss":bus1,"cars":car1}
    return render(request,"user/editvehicle.html",context)


def tour(request):
    packages=package.objects.all()
    context = {'packages' : packages}
    return render(request, "user/tour.html",context)


def addquery(request):
    user1 = userlogindata.objects.get(user=request.user)
    enq = request.POST['que1']
    myenq = Enquery(user=user1,enquerys=enq)
    myenq.save()
    return redirect('myenquiry')

def replyquery(request,taskid):
    myenq = Enquery.objects.get(id=taskid)
    print(myenq)
    rep1 = request.POST['reply1']
    myenq.reply=rep1
    myenq.status=True
    return redirect(request.META["HTTP_REFERER"])

