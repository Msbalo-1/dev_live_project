from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully login')
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR Password is Incorrect')
    return render(request, 'users/login_register.html')



def logoutUser(request):
    logout(request)
    messages.success(request, 'Successfully logout')
    return redirect('login')






def profiles(request):
    profile = Profile.objects.all()
    context = {'profile': profile}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile =Profile.objects.get(id=pk)
    TopSkills =profile.skill_set.exclude(description__exact="")
    OtherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'TopSkills': TopSkills, 'OtherSkills': OtherSkills}
    return render(request, 'users/user_profile.html', context)
