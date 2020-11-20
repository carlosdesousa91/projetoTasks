from django.shortcuts import render, redirect
from crudtasks.forms import TasksForm
from crudtasks.models import Tasks

#from django.http import HttpResponse, JsonResponse

def tas(request):
    if request.method == "GET":
        form = TasksForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
        else:
            form = TasksForm()
        return render(request,'index.html',{'form': form})
    #return HttpResponse("ok")
        
       
