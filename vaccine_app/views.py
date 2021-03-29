from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.models import  User,auth
from .models import VaccineLot, District, DistrictVaccineData, Center, CenterVaccineData, CenterRegestration, Receiver, ReceiverVaccination, AccessControlListCenter,AccessControlListDistrict
from datetime import datetime
from .models import User
from .forms import RegistrationForm, ProvideAccessForm
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import uuid
# Create your views here.
def index(request):
    # objs = [VaccineLot() for i in range(40)]
    # VaccineLot.objects.bulk_create(objs,batch_size=40)
    return render(request,"index.html")


def register_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        registerForm = RegistrationForm(request.POST)
        print("INside post")
        if registerForm.is_valid():
            print("Inside form")
            # user = registerForm.save(commit=False)
            center_name=registerForm.cleaned_data["center_name"]
            district_name=registerForm.cleaned_data["district_name"]
            key=registerForm.cleaned_data["key"]
            if center_name != "_":
                center_obj=Center.objects.get(name=center_name)
                if key==center_obj.centerId.urn[9:]:
                    user=User.objects.create(email=registerForm.cleaned_data["email"])
                    user.aadharNumber=registerForm.cleaned_data["aadharNumber"]
                    user.first_name=registerForm.cleaned_data["first_name"]
                    user.last_name=registerForm.cleaned_data["last_name"]
                    user.set_password(registerForm.cleaned_data["password"])
                    user.is_active = True
                    AccessControlListCenter.objects.create(
                        person=user,
                        center=center_obj
                    )
                    user.is_centeradmin=True
                    user.save()
                    center_obj.centerId=uuid.uuid4()
                    center_obj.save()
                    return redirect('dashboard')

            if district_name != "_":
                district_obj=District.objects.get(name=district_name)
                if key==district_obj.districtId.urn[9:]:
                    user=User.objects.create(email=registerForm.cleaned_data["email"])
                    user.aadharNumber=registerForm.cleaned_data["aadharNumber"]
                    user.first_name=registerForm.cleaned_data["first_name"]
                    user.last_name=registerForm.cleaned_data["last_name"]
                    user.set_password(registerForm.cleaned_data["password"])
                    user.is_active = True
                    AccessControlListDistrict.objects.create(
                        person=user,
                        district=district_obj
                    )
                    user.is_centeradmin=True
                    user.is_districtadmin=True
                    user.save()
                    district_obj.districtId=uuid.uuid4()
                    district_obj.save()
                    return redirect('dashboard')
            # user.save()

    else:
        registerForm = RegistrationForm()
    return render(request, "register.html", {"form": registerForm})


def logout(request):
    models.auth.logout(request)
    return redirect('/')
# def register_admin(request):
#     if request.user.is_authenticated:
#         return redirect('provide_access')

#     if request.method == "POST":
#         registerForm = RegistrationForm(request.POST)
#         print("INside post")
#         if registerForm.is_valid():
#             print("Inside form")
#             # user = registerForm.save(commit=False)
#             user=User.objects.create(email=registerForm.cleaned_data["email"])
#             user.aadharNumber=registerForm.cleaned_data["aadharNumber"]
#             user.first_name=registerForm.cleaned_data["first_name"]
#             user.last_name=registerForm.cleaned_data["last_name"]
#             user.set_password(registerForm.cleaned_data["password"])
#             user.is_active = True
#             user.save()
#             return redirect('provide_access')
#     else:
#         registerForm = RegistrationForm()
#     return render(request, "register.html", {"form": registerForm})

# def provide_access(request):
#     if request.user.is_authenticated:
        
#         return redirect('provide_access')
#     else:
#         return redirect('register_admin')
# def login_gen(request):
#     if request.user.is_authenticated:
#         return redirect('loggedin')
#     err=""
#     if request.method == 'POST':
#         username = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email = username, password = password)
#         if user is not None:
#             models.auth.login(request, user)
#             return redirect('loggedin')
#         else:
#            err = 'Input correct email and password'
#     template_name = 'login.html'
#     context={'err':err}
#     return render(request, template_name,context)



def login_gen(request):
    template_name = 'login.html'
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('dashboard')
        # if request.user.is_districtadmin:
        #     access_obj=AccessControlListDistrict.objects.get(person=request.user)
        #     redirect('/loggedin_district/district/'+access_obj.districtID.name)
        # elif request.user.is_centeradmin:
        #     access_obj=AccessControlListCenter.objects.get(person=request.user)
        #     redirect('/loggedin/center/'+access_obj.centerID.name)
        # else :
    error=[]
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        # center = request.POST.get('center')
        # district = request.POST.get('district')
        user = authenticate(request, email = username, password = password)
        
        #TODO add_drop_down and center selection
        # if center!="_" and district!="_":
        #     error.append("You can only login to one location, either district or center.")
        #     context={'error':error}
        #     return render(request, template_name,context)
        if user is not None:
            models.auth.login(request,user)
            return redirect('dashboard')
        else:
            error.append("Invalid User")

        # if user is not None:
        #     if center and center!="_":
        #         center_obj=Center.objects.filter(name=center)
        #         if center_obj.exists():
        #             center_obj=center_obj[0]
        #             if AccessControlListCenter.objects.filter(person=user,center=center_obj).exists() and user.is_centeradmin:
        #                 models.auth.login(request, user)
        #                 return redirect('/loggedin/center/'+center_obj.name)

        #             elif AccessControlListDistrict.objects.filter(person=user,district=center_obj.district).exists() and user.is_districtadmin:
        #                 models.auth.login(request, user)
        #                 return redirect('/loggedin/center/'+center_obj.name)
        #             else:
        #                 error.append("You don't have access to"+center_obj.name)
        #         else:
        #             error.append("Center Does not Exist")
        #         # center_obj=Center.objects.get(name=center)

        #     if district and district!="_":
        #         district_obj=District.objects.filter(name=district)
        #         if district_obj.exists():
        #             district_obj=district_obj[0]
        #             if AccessControlListDistrict.objects.filter(person=user,district=district_obj).exists() and user.is_districtadmin:
        #                 models.auth.login(request, user)
        #                 return redirect('/loggedin_district/district/'+district_obj.name)
        #             else:
        #                 error.append("You don't have access to"+district_obj.name)
        #         else:
        #             error.append("District does not exist")
                
        # else:
        #     error.append("invalid user")
    
    
    context={'error':error}
    return render(request, template_name,context)

@login_required(login_url="login_gen")
def dashboard(request):
    user=request.user
    # solve login
    # or remove
    center_access=AccessControlListCenter.objects.filter(person=user)
    # If user has access to only one center
    if not user.is_districtadmin and center_access.count()==1:
        # center_access=center_access[0]
        return redirect('/dashboard/center/'+center_access[0].center.name)


    if user.is_districtadmin:
        district_access=AccessControlListDistrict.objects.filter(person=user)
        center_name=[]
        district_name=[]
        for district in district_access:
            district_name.append(district.district.name)
            center_objs=Center.objects.filter(district=district.district)
            for center in center_objs:
                center_name.append(center.name)
        return render(request,'dashboard.html',{'centers':center_name,'districts':district_name})


        # redirect('/loggedin_district/district/'+access_obj.districtID.name)
    elif request.user.is_centeradmin and not user.is_districtadmin:
        center_name=[]
        district_name=[]
        for center in center_access:
            center_name.append(center.center.name)
        return render(request,'dashboard.html',{'centers':center_name,'districts':district_name})
    else :
        return redirect('login_gen')
    


# def loggedin(request,district_or_center,name):
#     # return HttpResponse("user is"+district_or_center+name)
#     if district_or_center=="district":
#         user=request.user
#         if District.objects.filter(name=name).exists():
#             district_obj=District.objects.get(name=name)
#             if AccessControlListDistrict.objects.filter(person=user,district=district_obj).exists() and user.is_districtadmin:
#                 return redirect('dashboard/district/'+district_obj.name)
#                 #TODO Make District Dashboard
#             else:
#                 return render(request,"fail.html")
#         else:
#             return render(request,"fail.html")
#     elif district_or_center=="center":
#         user=request.user
#         if Center.objects.filter(name=name).exists():
#             center_obj=Center.objects.get(name=name)
#             if AccessControlListCenter.objects.filter(person=user,center=center_obj).exists() and user.is_centeradmin:
#                 return HttpResponse("user is"+request.user.first_name+" Center "+name)
#             elif AccessControlListDistrict.objects.filter(person=user,district=center_obj.district).exists() and user.is_districtadmin:           
#                 return HttpResponse("user is"+request.user.first_name+" center "+center_obj.name)
#             else:
#                 return render(request,"fail.html")
#         else:
#             return render(request,"fail.html")
#     else:
#         return render(request,"fail.html")

@login_required(login_url="login_gen")
def provideaccess(request):
    if request.method == "POST":
        provide_access_form = ProvideAccessForm(request.user,request.POST)
        print("INside post")
        if provide_access_form.is_valid():
            print("Inside form")
            # user = registerForm.save(commit=False)
            center_name=provide_access_form.cleaned_data["center_name"]
            district_name=provide_access_form.cleaned_data["district_name"]
            key=provide_access_form.cleaned_data["key"]
            if center_name != "_":
                center_obj=Center.objects.get(name=center_name)
                if key==center_obj.centerId.urn[9:]:
                    
                    user=User.objects.get(email=request.user.email)
                    AccessControlListCenter.objects.create(
                        person=user,
                        center=center_obj
                    )
                    user.is_centeradmin=True
                    user.save()
                    center_obj.centerId=uuid.uuid4()
                    center_obj.save()
                    return redirect('dashboard')
            if district_name != "_":
                district_obj=District.objects.get(name=district_name)
                if key==district_obj.districtId.urn[9:]:
                    user=User.objects.get(email=request.user.email)
                    AccessControlListDistrict.objects.create(
                        person=user,
                        district=district_obj
                    )
                    user.is_centeradmin=True
                    user.is_districtadmin=True
                    user.save()
                    district_obj.districtId=uuid.uuid4()
                    district_obj.save()
                    return redirect('dashboard')
            # user.save()

    else:
        provide_access_form = ProvideAccessForm(request.user)
    return render(request, "provideaccess.html", {"form": provide_access_form})

def verify(request,district_or_center,name):
    if district_or_center=="district":
        user=request.user
        if District.objects.filter(name=name).exists():
            district_obj=District.objects.get(name=name)
            if AccessControlListDistrict.objects.filter(person=user,district=district_obj).exists() and user.is_districtadmin:
                return True
            else:
                print("access is not there for user "+user.email)
                return False
        else:
            print("District name is invalid")
            return False
    elif district_or_center=="center":
        user=request.user
        if Center.objects.filter(name=name).exists():
            center_obj=Center.objects.get(name=name)
            if AccessControlListCenter.objects.filter(person=user,center=center_obj).exists() and user.is_centeradmin:
                return True
            elif AccessControlListDistrict.objects.filter(person=user,district=center_obj.district).exists() and user.is_districtadmin:
                return True
            else:
                print("access not present "+user.email)
                return False
        else:
            print("center name does not exist")
            return False
    else:
        print("Invalid district_or_center value")
        return False



@login_required
def district_dash(request,name):
    if name=="":
        return redirect('dashboard')
    if verify(request,"district",name):
        district_obj=District.objects.filter(name=name)
        dist = AccessControlListDistrict.objects.get(person = request.user,district=district_obj[0])
        dist_ID = dist.district
        centers = Center.objects.filter(district=dist_ID)
        error=[]
        if request.method=="POST":
            nameCenter = request.POST['name']
            
            if(nameCenter!=""):
                centeradd_obj=Center.objects.filter(name=nameCenter)
                district_name=name
                district_obj=District.objects.get(name=name)
                if centeradd_obj.exists():
                    error.append("Center Already Exists")
                else:
                    new_center=Center(name=nameCenter,district=district_obj)
                    new_center.save()

                name=""
        
        return render(request,'district_dash.html',{'centers':centers,'error':error})
    else:
        return redirect('dashboard')





@login_required
def center_dash(request,name):
    if name=="":
        return redirect('dashboard')
    if verify(request,"center",name):


        return HttpResponse("Center name: "+name+"\nUser Name: "+request.user.first_name)
    else:
        return redirect('dashboard')











#TODO verify function, clean templates
#TODO loggedin page where you can access all the places where you have access. If count equals to one admin of only one place
#go straight to that place

# TODO update uuid
# 