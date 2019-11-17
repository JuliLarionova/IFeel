from rest_framework.response import Response
from rest_framework.views import APIView

from IFeel import models


class MakeQuestionary(APIView):
    def post(self, request, template_id):
        template = models.Template.objects.get(id=template_id)
        questionary = models.Questionary(template=template, author=request.user)
        questionary.save()

        return Response(questionary.to_json())


class TemplatesView(APIView):
    def get(self, request):
        forms = models.Template.objects.all()
        return Response(list([{"name": x.name, "id": x.id} for x in forms]))
