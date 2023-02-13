from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.


def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username OR Password is Incorrect')



    return render(request, 'users/login_register.html')



def logoutUser(request):
    logout(request)
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
