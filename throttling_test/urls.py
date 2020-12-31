
from django.urls import  path, include
from .views import StudentModelViewSet
from rest_framework.routers import DefaultRouter

# creating router objects 
router = DefaultRouter()
# Register StudentViewSet with Router
router.register('student_api',StudentModelViewSet,basename = 'student')




urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))

]