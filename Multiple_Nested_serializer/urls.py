
from django.urls import  path, include
from .views import MainWhoweAreViewSet,OurStoryViewSet, OurServiceViewSet
from rest_framework.routers import DefaultRouter

# creating router objects 
router = DefaultRouter()
# Register StudentViewSet with Router
router.register('who_we_are',MainWhoweAreViewSet,basename = 'Who')
router.register('ourstory',OurStoryViewSet,basename = 'story')
router.register('OurService', OurServiceViewSet, basename = 'service')




urlpatterns = [
    path('', include(router.urls)),

]