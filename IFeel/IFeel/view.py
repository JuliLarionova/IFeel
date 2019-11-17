import os

from rest_framework import status, serializers
from rest_framework.parsers import FileUploadParser, MultiPartParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from IFeel import models

UPLOAD_DIRECTORY = "/home/julia/Work"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


class AudioFileView(APIView):
    def post(self, request):
        audio = request.data.get("")
        return Response({"audio": ['sgsdg']})


class TemplatesView(APIView):
    def get(self, request):
        forms = models.Template.objects.all()
        return Response({
            "forms": list([{"name": x.name, "id": x.id} for x in forms]),
        })


class FileUploadSerializer(serializers.Serializer):
    # I set use_url to False so I don't need to pass file
    # through the url itself - defaults to True if you need it
    file = serializers.FileField()


class FilesView(APIView):

    def post(self, request):
        up_file_list = request.FILES.getlist('data')
        for file in up_file_list:
            def

