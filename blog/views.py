from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import blog_technology
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def allblogs(request):
    blog_technology_var=blog_technology.objects
    return render(request,'blogs/allblogs.html',{'blog_technology_key':blog_technology_var})
def detail(request,blog_id):
    detailblogT =get_object_or_404(blog_technology,pk=blog_id)
    return render(request,'blogs/detail.html',{'detailkeyT':detailblogT})


@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('allblogs'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'blogs/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('blogsname'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'blogs/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog')