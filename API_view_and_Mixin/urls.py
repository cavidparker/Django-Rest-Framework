from django.urls import  path
# from .views import MainCanvasList,MainCanvasRetriveAPIView,MainHomepageList
from .views import StudentListAndCreateAPI,StudentRetrieveUpdateDelete

urlpatterns = [
    path('mixin_api_List_and_update/',StudentListAndCreateAPI.as_view()),
    path('mixin_api_List_and_update/<int:pk>/',StudentRetrieveUpdateDelete.as_view()),



]
