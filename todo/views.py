from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks
# Create your views here.

def home(request):
    # m =  Tasks('learnCrud')
    # m.save()
    Entries = Tasks.objects.all()
    #Entries = {'hello'}

    return render(request,"index.html",{'ent':Entries})


def create_read(request, *args, **kwargs):
    content = None
    if request.method == 'GET':
        content = request.GET['key']

        p = Tasks(task = content)
        p.save()
        return HttpResponse('success')

    else:
        return HttpResponse('Fail')

def delete_instance(request,*args, **kwargs):
    instance = None
    if request.method == 'GET':
        instance = request.GET['key']

        m = Tasks.objects.get(task=instance)
        m.delete()
        Entries = Tasks.objects.all()
        return render(request,"index.html",{'ent':Entries})
    else:
        return HttpResponse('Fail')


def update_instance(request,*args,**kwargs):
    instance = None
    if request.method == 'GET':
        instance = request.GET['key']
        print(str(instance))
        obj = instance.split('/')
        initial = obj[0]
        final = obj[1]
        print(obj)
        print(initial)
        print(final)
        m1 = Tasks.objects.get(task=initial)
        m2 = Tasks.objects.get(task=initial)
        m1.task = final
        m1.save()
        m2.delete()
        Entries = Tasks.objects.all()
        return render(request,"index.html",{'ent':Entries})
    else:
        return HttpResponse('Fail')
