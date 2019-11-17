from rest_framework.response import Response
from rest_framework.views import APIView

from IFeel import models


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
