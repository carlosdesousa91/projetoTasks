from django.http import HttpResponse, JsonResponse
from tasks.fazer.models import Fazer
from tasks.fazer.serializers import FazerSerializer
from rest_framework import viewsets

class FazerViewSet(viewsets.ModelViewSet):
    queryset = Fazer.objects.all()
    serializer_class = FazerSerializer

"""def fazer(request):
    if request.method == 'GET':
        #return HttpResponse("ok")
        fazer = Fazer.objects.first()
        serializer = FazerSerializer(fazer)
        return JsonResponse(serializer.data)"""
