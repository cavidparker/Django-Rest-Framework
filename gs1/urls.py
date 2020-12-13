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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/<int:pk>', views.Student_detail),
    path('student_info/',views.Student_list),
    path('student_create/', sv.Student_create),
    path('student_list_two/', sv.Student_list_two),
]
