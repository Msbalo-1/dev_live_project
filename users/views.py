from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import customUserCreationForm, profileForm, skillForm, messageForm
from django.contrib.auth.models import User
from .models import Profile, Message
from .utils import searchProfile, profilePaginator
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
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
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

            return redirect('edit_account')

        else:
            messages.error(request, 'An Error Occurred when Registering')
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profile, search_query = searchProfile(request)
    custom_range, profile = profilePaginator(request, profile, 3)

    context = {'profile': profile, 'search_query': search_query, 'custom_range': custom_range, }
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile =Profile.objects.get(id=pk)
    # projects = profile.project_set.all(id=pk)
    TopSkills =profile.skill_set.exclude(description__exact="")
    OtherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'TopSkills': TopSkills, 'OtherSkills': OtherSkills}
    return render(request, 'users/user_profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = profileForm(instance=profile)

    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Successfully Edited')
            return redirect('account')


    context = {'form': form}

    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = skillForm()

    if request.method == 'POST':
        form = skillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill Successfully Created')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def editSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = skillForm(instance=skill)

    if request.method == 'POST':
        form = skillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill Successfully Edited')
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Project Successfully Deleted')
        return redirect('account')
    return render(request, 'projects/delete-project.html', {'object': skill})


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadRequest = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadRequest': unreadRequest}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def messageRecived(requset, pk):

    profile = requset.user.profile
    # sender = profile
    message = profile.messages.get(id=pk)

    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(requset, 'users/messages.html', context)




def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = messageForm()
    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email

            message.save()
            messages.success(request, 'Your Message was Successfully Sent')
            return redirect('user_profile', pk=recipient.id)



    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/messages_form.html', context)



