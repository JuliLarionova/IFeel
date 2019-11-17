from wit import Wit

client = Wit('ESGLK6TZWBGQR2MQ5V55747RU2YP4345')
with open('/home/julia/Documents/test_audio.mp3', 'rb') as f:
   resp = client.speech(f, None, {'Content-Type': 'audio/mpeg3'})
print('Inserting values of {}'.format(resp))

def read_file(file):

   resp = client.speech(f, None, {'Content-Type': 'audio/mpeg3'})
