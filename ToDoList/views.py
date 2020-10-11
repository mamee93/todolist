from django.shortcuts import render,redirect
from .models import ToDoList
from .forms import AdListForm

# Create your views here.

def list(request):
    list = ToDoList.objects.all()
    form = AdListForm()
    if request.method == "POST":
        form = AdListForm(request.POST)
        if form.is_valid():
            myform = form.save()
        return redirect('/')

    return render(request, 'ToDoList.html',{'form':form,'list':list})


def update_list(request, pk):
    listup = ToDoList.objects.get(id=pk)
    form = AdListForm(instance=listup)

    if request.method == 'POST':
        form = AdListForm(request.POST, instance=listup)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update_list.html', {'form':form})




def delete_list(request,id):
    Dlist = ToDoList.objects.get(id=id)
    if request.method == 'POST':
        Dlist.delete()
        return redirect('/')

    return render(request,'delete.html',{'Dlist':Dlist})
 

