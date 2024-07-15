from django.shortcuts import render, HttpResponse , redirect , get_object_or_404
from home.models import Task

# Create your views here.
def home(request):
    context ={ 'success': False}
    if request.method == "POST":
        #handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins= Task(TASKTITLE=title,TASKDESC=desc)
        ins.save()
        context ={ 'success': True}

    return render(request,'index.html',context)

def task(request):
    allTask =Task.objects.all()
    print(allTask)
    for item in allTask:
        print(item.TASKTITLE)
    context={'task': allTask}
    return render(request,'task.html', context)


