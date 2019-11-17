from wit import Wit
import magic
import tempfile


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
