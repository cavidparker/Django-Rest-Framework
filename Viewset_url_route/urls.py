
from django.urls import  path, include
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

# creating router objects 
router = DefaultRouter()
# Register StudentViewSet with Router
router.register('student_viewset_url',StudentViewSet,basename = 'studentviewsetapi')





urlpatterns = [
    path('', include(router.urls)),

]