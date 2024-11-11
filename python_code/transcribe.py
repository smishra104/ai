from openai import OpenAI
from openai_connector import setup_openai

def transcribe_audio(audio_filepath):
    client = setup_openai()
    system_prompt = f'''You include a summary sentence at the beginning of the audio.'''
    audio_file= open(audio_filepath, "rb")

    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        response_format="verbose_json",
        timestamp_granularities=["word"]
    )

    return transcription.text
