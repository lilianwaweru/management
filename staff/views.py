from django.shortcuts import render,redirect
from .models import Master as MasterModel
from .forms import MasterForm

# Create your views here.
def index(request):
    return render(request, "index.html")


def employee(request):
    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
        return redirect('view_employee') 
    else:
        form = MasterForm()

    return render(request, 'employee.html',{'form':form}) 


def view_employee(request):
    masters = MasterModel.objects.all()
    print(masters)
    return render(request,'view_employee.html',{"masters":masters}) 


