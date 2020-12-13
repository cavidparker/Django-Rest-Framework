from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Student
from django.http import HttpResponse, JsonResponse

# Create your views here.
# student send Data into the database:
@csrf_exempt
def Student_create(request):
    if request.method =='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)    
        return HttpResponse(json_data, content_type='application/json')


# all Student show send Data :

def Student_list_two(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe = False)        