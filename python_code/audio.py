from openai import OpenAI
from openai_connector import setup_openai
# from pydub import AudioSegment

def convert_to_audio(filepath, input):
    client = setup_openai()
    with open(filepath, 'wb') as audio_file:
        response = client.audio.speech.create(
            model = 'tts-1',
            voice = 'alloy',
            input = input
        )
        response.stream_to_file(filepath)


convert_to_audio("bday.mp3", "Ha Ha Ha Happy Birthday John Doe")