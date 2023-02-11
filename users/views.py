from django.shortcuts import render
from .models import Profile
# Create your views here.

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
