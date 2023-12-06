from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from zaid.settings import MEDIA_ROOT
from .models import Driverwork
# Create your views here.
users=''
ids=''
name=''
def index(request):
    return render(request,'index.html')

def login(request):
    try:
        global users,ids,name
        driverid=request.POST.get('driverid')
        password=request.POST.get('password')
        user=Users.objects.filter(driverid=driverid).values()
        users=user[0]['driverid']
        name=user[0]['name']
        if user[0]['password']==password and user[0]['isadmin'].lower()=='yes':
            return redirect('admin:index')
        elif user[0]['password']==password:
            data=Driverwork.objects.filter(driverid=driverid).values()
            return render(request,'display.html',{'data':data})
        else:
            return index(request)
    except Exception as e:
        return index(request)
    
def addition(request): 
        corp=Corporate.objects.distinct().values()
        Places1=Places.objects.distinct().values()
        print(Places1)
        return render(request,'form.html',{'user':users,'corp':corp,'name':name,'corp1':Places1})


def addition2(request):
    global ids
    ids=request.POST['ided']
    return render(request,'form2.html')
def formapp2(request):
    try:
        global users,ids
        user=Driverwork.objects.get(id=int(ids))
        user.update=True
        user.gatepassno=request.POST['gatepassno']
        user.save()
        data=Driverwork.objects.filter(driverid=users).values()
        return render(request,'display.html',{'data':data})
    except Exception as e: 
        Places1=Places.objects.distinct().values()
        return render(request,'form2.html',{'corp':Places1})
        pass
def formapp(request):
    try:
        driverid=request.POST['driver_id']
        corporate=request.POST.get('corporate')
        loaction=request.POST.get('location')
        date=request.POST.get('date')
        name=request.POST.get('name')
        pickup=request.POST.get('pick_up_place')
        drop=request.POST.get('drop_place')
        vehicleno=request.POST.get('vehicle_no')
        p=request.FILES.get('image').name
        print(p)
        user=Driverwork(driverid=users,corporatename=corporate,location=loaction,date=date,name=name,pickupplace=pickup,dropplace=drop,vehicleno=vehicleno,photo=request.FILES.get('image'),update=False)
        user.save()
        image_path = os.path.join(MEDIA_ROOT, p)
        print(image_path)
        print(os.path.exists(image_path))
        # Delete the image file from the filesystem
        if os.path.exists(image_path):
            print('yes')
            os.remove(image_path)
        data=Driverwork.objects.filter(driverid=driverid).values()
        return render(request,'display.html',{'data':data})
    except Exception as e:
        print(e) 
        corp=Corporate.objects.distinct().values()
        Places1=Places.objects.distinct().values()
        print(Places1)
        return render(request,'form.html',{'user':users,'corp':corp,'name':name,'corp1':Places1})
        return render(request,'form.html')
    
