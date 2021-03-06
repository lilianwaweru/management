from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import index

urlpatterns = [
    
    path("",views.index,name="home"),
    # path("employee/",views.employee,name="employee"),
    # path("view_employee/",views.view_employee,name="view_employee"),
    path("work/",views.work,name="work"),
    path("experience/",views.experience,name="experience")
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)