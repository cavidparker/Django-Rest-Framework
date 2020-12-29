
from django.urls import  path
from .views import StudentListCreate,StudentRetrieveUpdateDestroy


urlpatterns = [
    path('Concrete_List_and_update/',StudentListCreate.as_view()),
    path('Concrete_List_and_update/<int:pk>/', StudentRetrieveUpdateDestroy.as_view()),

]