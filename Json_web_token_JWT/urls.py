
from django.urls import  path, include
from .views import StudentModelViewSet
from rest_framework.routers import DefaultRouter
# from rest_framework_jwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView



# creating router objects 
router = DefaultRouter()
## Register StudentViewSet with Router
router.register('student_api',StudentModelViewSet,basename = 'student')




urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('gettoken/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),


]
# create token:
# http POST http://127.0.0.1:8000/token_JWT/gettoken/ username="max" password="alienide"

# verify token
# http POST http://127.0.0.1:8000/token_JWT/verifytoken/ token="your token"

# refresh token
# http POST http://127.0.0.1:8000/token_JWT/refreshtoken/ refresh="your refresh token"

# GET result :
# http http://127.0.0.1:8000/token_JWT/student_api/ 'Authorization:Bearer yourtoken' 

# POST Request:
# http -f POST http://127.0.0.1:8000/token_JWT/student_api/ name=parker roll=103 city=LA 'Authorization:Bearer yourtoken'

# Update Request:
# http -f PUT http://127.0.0.1:8000/token_JWT/student_api/3/ name=cavidparker roll=104 city=LA 'Authorization:Bearer yourtoken'

# Delete Request:
# http -f DELETE http://127.0.0.1:8000/token_JWT/student_api/2/ 'Authorization:Bearer yourtoken'




