import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
import json

from django.views.decorators.csrf import csrf_exempt
from requests import Response

from subjects.models import subjects, Curse, Task
from .models import Profile, TaskProfile


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


def token(request):
    if ('error' in request.GET):
        return redirect('http://127.0.0.1:3000')
    code = request.GET['code']
    test = requests.get(
        'https://oauth.vk.com/access_token?client_id=51587230&client_secret=Voo3Kq3PI3xKoeDGp8DV&redirect_uri=http://127.0.0.1:8000/token&code=' + code)
    json_token = json.loads(test.text)["access_token"]
    data = requests.post('http://127.0.0.1:8000/auth/convert-token', data={
        "grant_type": "convert_token",
        "client_id": "sE36wkEE0pvSxIpobxF96riPvuM54jHsopcrG4pj",
        "token": "" + json_token,
        "backend": "vk-oauth2"})
    json_token_bd = json.loads((data.text))['access_token']
    content = {'data': json_token_bd}
    return redirect('http://127.0.0.1:3000/login?token=' + json_token_bd)


@csrf_exempt
def analysAnswer(request):
    d = json.loads(request.body)
    result = {"answer": "true", "task": d['idTask']}
    result2 = {"answer": "false"}
    model = Task.objects.get(id=d['idTask'])
    if (model.answer == float(d['answer'])):
        create = TaskProfile.objects.create(
            solveTask=True,
            task_id=int(d['idTask']),
            profile_id=int(d['idProfile'])
        )
        create.save()
        return HttpResponse(json.dumps(result), content_type="application/json")
    else:
        return HttpResponse(json.dumps(result2), content_type="application/json")
