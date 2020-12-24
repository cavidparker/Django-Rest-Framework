from django.urls import  path
# from .views import MainCanvasList,MainCanvasRetriveAPIView,MainHomepageList
from .views import StudentAPI

urlpatterns = [
    path('class_based_api_view/',StudentAPI.as_view()),
    path('class_based_api_view/<int:pk>/',StudentAPI.as_view()),

]
