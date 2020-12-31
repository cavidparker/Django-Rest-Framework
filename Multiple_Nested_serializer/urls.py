
from django.urls import  path, include
from .views import MainWhoweAreViewSet,OurStoryViewSet
from rest_framework.routers import DefaultRouter

# creating router objects 
router = DefaultRouter()
# Register StudentViewSet with Router
router.register('who_we_are',MainWhoweAreViewSet,basename = 'Who')
router.register('ourstory',OurStoryViewSet,basename = 'story')




urlpatterns = [
    path('', include(router.urls)),

]