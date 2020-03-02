from django.shortcuts import render,redirect
# from .models import Master as MasterModel
# from django.contrib.auth.decorators import login_required
from .models import Work as WorkModel
from .forms import WorkForm

# Create your views here.





def index(request):
    return render(request, "index.html")

#employees
# def employee(request):
#     if request.method == 'POST':
#         form = MasterForm(request.POST)
#         if form.is_valid():
#             create = form.save(commit=False)
#             create.save()
#         return redirect('view_employee') 
#     else:
#         form = MasterForm()

#     return render(request, 'employee.html',{'form':form}) 


# def view_employee(request):
#     masters = MasterModel.objects.all()
    
#     return render(request,'view_employee.html',{"masters":masters}) 

#end of employees


#work
def work(request):
    

    if request.method == 'POST':
        
        form = WorkForm(request.POST,request.FILES)
        if form.is_valid():
            create = form.save(commit=False)
            
            create.save()
        return redirect('experience') 
    else:
        form = WorkForm()

    return render(request, 'work.html',{'form':form}) 



def experience(request):
    works = WorkModel.objects.all()
    for i in works:
        print (i.image)
    
    return render(request,'experience.html',{"works":works}) 
