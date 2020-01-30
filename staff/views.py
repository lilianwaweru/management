from django.shortcuts import render,redirect
from .models import Master as MasterModel
from .models import Education as EducationModel
from .models import Work as WorkModel
from .forms import MasterForm,EducationForm,WorkForm

# Create your views here.
def index(request):
    return render(request, "index.html")

#employees
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

#end of employees

#education
def education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
        return redirect('view_education') 
    else:
        form = EducationForm()

    return render(request, 'education.html',{'form':form}) 


def view_education(request):
    educations = EducationModel.objects.all()
    print(educations)
    return render(request,'view_education.html',{"educations":educations}) 

#end of education

#work
def work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
        return redirect('experience') 
    else:
        form = WorkForm()

    return render(request, 'work.html',{'form':form}) 

def experience(request):
    works = WorkModel.objects.all()
    print(works)
    return render(request,'experience.html',{"works":works}) 
