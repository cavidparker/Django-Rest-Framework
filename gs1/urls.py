"""gs1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from DeserializationApi import views as sv
from CRUD_Func_based import views as CRUD_views
from CRUD_Class_based import views as CRUD_class_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/<int:pk>', views.Student_detail),
    path('student_info/',views.Student_list),
    path('student_create/', sv.Student_create),
    path('student_list/', sv.Student_list_two),
    path('crud_get_api/', CRUD_views.student_api),
    path('crud_func_list/', CRUD_views.crud_func_list),
    path('crud_class_list/', CRUD_class_views.StudentApi.as_view()),



]
