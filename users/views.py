from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import customUserCreationForm
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.


def loginUser(request):
    page = 'register'

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
    messages.info(request, 'Successfully logout')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = customUserCreationForm()

    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Account was Successfully Created')

            login(request, user)

            return redirect('profiles')

        else:
            messages.error(request, 'An Error Occurred when Registering')



    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)





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
