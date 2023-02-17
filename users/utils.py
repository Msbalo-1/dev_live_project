from django.db.models import Q
from .models import Profile, Skill

def searchProfile(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__iexact=search_query)
    profile = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(shot_intro__icontains=search_query) |
        Q(skill__in=skills)
    )
    return profile, search_query


