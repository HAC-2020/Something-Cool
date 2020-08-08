from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import BioSerializer, BioSerializer2
from .models import BioOutput


# Create your views here.
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = BioOutput.objects.all()
        post = qs.first()
        #serializer = BioSerializer(qs,many=True)
        serializer = BioSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Test2View(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BioSerializer2(data = request.data)
        if serializer.is_valid():
            serializer.save()
            #############################
            #
            # This is where the ML algorithims will go
            #Once we find out what the inputs will be then
            # we will go to models.py and change what we need
            # then we will go to serializers and put in the specific 
            # variables we want
            #
            return Response(serializer.data["num1"]+serializer.data["num2"])
        return Response(serializer.errors)
        
        
        
        #num3 = num1 + num2
     



#def test_view(request):
#    data = {
#        'name':'daniel',
#        'age':'25'
#    }
#    return JsonResponse(data)