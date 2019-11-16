from rest_framework.response import Response
from rest_framework.views import APIView

class AudioFileView():
    def get(self, request):
        return Response({"audio": ['sgsdg']})