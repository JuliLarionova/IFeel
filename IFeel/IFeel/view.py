from rest_framework.response import Response
from rest_framework.views import APIView

from IFeel import models
from IFeel.utils import SpechToText


class MakeQuestionaryView(APIView):
    def post(self, request, template_id,  *args, **kwargs):
        template = models.Template.objects.get(id=template_id)
        questionary = models.Questionary(template=template, author=request.user)
        questionary.save()

        return Response(questionary.to_json())


class TemplatesView(APIView):
    def get(self, request,  *args, **kwargs):
        forms = models.Template.objects.all()
        return Response(list([x.to_json() for x in forms]))


class UpdateQuestionaryView(APIView):
    def post(self, request, questionary_id, *args, **kwargs):
        questionary = models.Questionary.objects.get(id=questionary_id)
        if not request.user or questionary.author_id != request.user.id:
            return Response(status=400)
        if request.FILES:
            stt = SpechToText()
            up_file_list = request.FILES.getlist('files')
            for file in up_file_list:
                text = stt.get_text(file)
        else:
            pass


        return Response(status=)

