from django.shortcuts import render
from .models import subjects, Curse
def subj(request):
   subj = subjects.objects.all()
   return render(request,'main/index.html', {'subj':subj})
