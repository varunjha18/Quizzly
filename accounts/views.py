from accounts.models import User_profile
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(username=email,password=password)

        if user is not None:
            auth.login(request,user)
            # print('you are logged in')
            messages.success(request,'you are logged in')
            return redirect('home')

        else:
            # messages.error(request,'invalid login credentials')
            print('invalid login credential')
            return redirect('login')

    else:
        return render(request,'login.html')


    # return render(request,'accounts/login.html')



def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        college=request.POST['college']
        year_study=request.POST['year_study']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
    
        if password == confirm_password:
            if User.objects.filter(username=email).exists():
                # messages.error(request,"Username already exists")
                print("Username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    # messages.error(request,"email already exists")
                    print("email already exists")
                    return redirect('register')

                else:
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=email,password=password)
                    auth.login(request,user)
                    user.save()
                    profile=User_profile(user_id=user.id,user_name=first_name+' '+last_name,college=college,year_study=year_study)
                    profile.save()
                    # print("you are logged in")
                    # messages.success(request,"you are registered")
                    return redirect('home')
                    

        else:
            # messages.error(request,"password not matched")
            print("password not matched")
            return redirect('register')

    else:
        return render(request,'register.html')



def logout(request):
    # if request.method=="POST":
    auth.logout(request)
    messages.success(request,'you are logged out')
        # return redirect('home')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    user_id=request.user.id
    this_user=get_object_or_404(User_profile,user_id=user_id)
    # print('hhhhhhhhhheeeeeeeeeeeeeeerrrrrrrrrrrrrrrrreeeeeeeeeeeeeeeee')
    # print(user)
    if request.method=='POST':
        if request.POST['user_name']:
            this_user.user_name=request.POST['user_name']
        if request.POST['college']:
            this_user.college=request.POST['college']
        if request.POST['year_study']:
            this_user.year_study=request.POST['year_study']
        if request.FILES.get('profile_img') is not None:
            this_user.profile_img=request.FILES.get('profile_img')
        # print(request.FILES.get('profile_img'))
        this_user.save()

    data={'user':this_user,}
    print(User.is_authenticated)
    return render(request,'dashboard.html',data)


def test_site(request):
    return render(request,'test_site.html')