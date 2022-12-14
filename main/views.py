from django.shortcuts import render
from subjects.models import subjects, Curse
from .models import Profile


def index(request):
    subj = subjects.objects.all()
    # kurses = Curse.objects.all()
    # if len(condition['']) > 2:
    #     kurses = Curse.objects.filter(subject_id=condition[''])
    kurses = Curse.objects.all()
    return render(request, 'main/index.html', {'subj': subj, 'kurs': kurses})


def profile(request):
    profile_user = Profile.objects.filter(name=request.user)
    return render(request, 'main/profile.html', {'profile': profile_user})

def subjectInAccount(request):
    return render(request, 'main/coursesInProfile.html')
