from django.urls import  path, include
from .views import TextAPIView


urlpatterns = [
    path('multi_model_api/', TextAPIView.as_view(),name='multi_model'),
]