import numbers

import requests
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
import json

from django.views.decorators.csrf import csrf_exempt
from requests import Response

from subjects.models import subjects, Curse, Task
from .models import Profile, TaskProfile, Enrollment


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
        return redirect('http://localhost:3000')
    code = request.GET['code']
    test = requests.get(
        'https://oauth.vk.com/access_token?client_id=51587230&client_secret=Voo3Kq3PI3xKoeDGp8DV&redirect_uri=http://localhost:8000/token&code=' + code)
    json_token = json.loads(test.text)["access_token"]
    data = requests.post('http://localhost:8000/auth/convert-token', data={
        "grant_type": "convert_token",
        "client_id": "fL62vDDONghEKn5rQ1futIOg10PVCeSRZDFIFtpm",
        "token": "" + json_token,
        "backend": "vk-oauth2"})
    json_token_bd = json.loads((data.text))['access_token']
    content = {'data': json_token_bd}
    return redirect('http://localhost:3000/login?token=' + json_token_bd)


@csrf_exempt
def analysAnswer(request):
    d = json.loads(request.body)
    if (d['answer'].replace('.', '', 1).isdigit()):
        result = {"answer": "true", "task": d['idTask'], "color": "green", "res": "Ответ верный!", "id": d['idTask']}
        model = Task.objects.get(id=d['idTask'])
        if TaskProfile.objects.filter(profile_id=d['idProfile']) & TaskProfile.objects.filter(
                task_id=d['idTask']):
            return HttpResponse(
                json.dumps({"res": "Вы уже ответили правильно на это задание!", "color": "green", "id": d['idTask']}),
                content_type="application/json")
        if (model.answer == float(d['answer'])):
            create = TaskProfile.objects.create(
                solveTask=True,
                task_id=int(d['idTask']),
                profile_id=int(d['idProfile'])
            )
            create.save()
            return HttpResponse(json.dumps(result), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"res": "Ответ не верный!!", "color": "red", "id": d['idTask']}),
                                content_type="application/json")
    else:
        return HttpResponse(json.dumps({"res": "Введите только число!", "color": "purple", "id": d['idTask']}),
                            content_type="application/json")


def statistics(request, pk):
    model = TaskProfile.objects.filter(profile_id=pk).count()
    allTask = Task.objects.all().count()
    statistic = model / allTask * 100
    return HttpResponse(json.dumps({"statistic": statistic}), content_type="application/json")


def check_live(request):
    result = requests.get('https://player.twitch.tv/?channel=dinol_bot&muted=true&parent=127.0.0.1')
    return result


def order_by(request):
    value = Enrollment.objects.values('curse_id').annotate(course_count=Count('curse_id')).order_by('-course_count')
    return JsonResponse({"obj": list(value)})


@csrf_exempt
def userInCourse(request):
    answer = json.loads(request.body)
    value = Enrollment.objects.filter(profile_id=answer['profile_id'], curse_id=answer['curse_id'])
    if (value.count() > 0):
        return JsonResponse({"result": 'true'})
    else:
        return JsonResponse({"result": 'false'})


@csrf_exempt
def file(request):
    return JsonResponse({"ans": "good"})
