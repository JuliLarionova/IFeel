from cgitb import text

from wit import Wit
import magic
import tempfile

from IFeel import models


class SpeechMimeException(Exception):
    pass


class SpechToText(object):
    client = Wit('ESGLK6TZWBGQR2MQ5V55747RU2YP4345')
    mime = magic.Magic(mime=True)
    TRUE_MIMES = ('audio/wav', 'audio/mpeg3', 'audio/ogg', 'audio/ulaw', 'audio/raw', 'audio/mpeg')

    def get_file_name(self, speech_file):
        fn = tempfile.mktemp(speech_file.name)
        with open(fn, 'wb') as f:
            f.write(speech_file.open('rb').read())
            speech_file.close()
        return fn

    def check_mime(self, filename):
        m = self.mime.from_file(filename)
        if m in self.TRUE_MIMES:
            return m

    def get_text(self, speech_file):
        fn = self.get_file_name(speech_file)
        mm = self.check_mime(fn)
        if not mm:
            raise SpeechMimeException()
        with open(fn, 'rb') as f:
            resp = self.client.speech(f, None, {'Content-Type': mm})
        return resp


    def parse_text(self, questionary, text):
        questionary_fields = models.QuestionaryField.objects.all()
        for field in questionary_fields:
            print(text)
            print(field.speech_code)
            if field.speech_code.lower() in text:
                field_id = models.QuestionaryField.objects.get(speech_code=field.speech_code.lower())
                field_value = models.FieldValue.objects.get_or_create(field_id=field_id, questionary_id=questionary.id)
                #field_value = models.FieldValue(value="", field_id=field.id, questionary_id=questionary.id)

                if "значе" in text:
                    startInd = text.find("значени") + 9
                    str_len = len(text)
                    field_value.value = text[startInd: startInd + (str_len-startInd)]

                field_value.save()
