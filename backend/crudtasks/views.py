from django.shortcuts import render, redirect
from crudtasks.forms import TasksForm
from crudtasks.models import Tasks


#from django.http import HttpResponse, JsonResponse

def tas(request):
    if request.method == "POST":
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

def view(request):
    tasks = Tasks.objects.all()
    return render(request, "view.html", {'tasks': tasks})

def delete(request, id):
    tasks = Tasks.objects.get(id=id)
    tasks.delete()
    return redirect("/view")

def edit(request, id):
    tasks = Tasks.objects.get(id=id)
    return render(request, 'edit.html', {'tasks':tasks})

def update(request, id):
    tasks = Tasks.objects.get(id=id)
    form = TasksForm(request.POST, instance = tasks)  
    if form.is_valid():  
        form.save()  
        return redirect("/view")  
    return render(request, 'edit.html', {'tasks': tasks})
    
    
        
       
