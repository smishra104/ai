from pytubefix import YouTube
import uuid
from transcribe import transcribe_audio
from chat import translate
import os

OUTPUT_FOLDER = "output"

def download_youtube_audio(video_url, download_folder="."):
    try:
        # Create a YouTube object with the URL
        yt = YouTube(video_url)
        
        # Select the highest resolution stream available
        video_stream = yt.streams.get_audio_only()
        
        # Download the video to the specified path
        print(f"Downloading audio: {yt.title}")
        file_path = video_stream.download(mp3=True, output_path=download_folder)
        
        print("Download completed!")
        return file_path
    except Exception as e:
        print(f"An error occurred: {e}")

def download_youtube_video(video_url, download_folder="."):
    try:
        # Create a YouTube object with the URL
        yt = YouTube(video_url)
        
        # Select the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()
        
        # Download the video to the specified path
        print(f"Downloading video: {yt.title}")
        file_path = video_stream.download(output_path=download_folder)
        
        print("Download completed!")
        return file_path
    except Exception as e:
        print(f"An error occurred: {e}")

def create_folder():
    import os
    full_path = OUTPUT_FOLDER + '/' + str(uuid.uuid4())
    os.makedirs(full_path)
    return full_path

def write_to_file(download_folder, filename, text):
    file_path = os.path.join(download_folder, filename)
    with open(file_path, 'w') as file:
        file.write(text)

if __name__ == "__main__":
    download_folder = create_folder()
    video_url = "https://www.youtube.com/watch?v=ClC4s6EXyn4"
    # # download_youtube_video(video_url, download_folder)
    audio_file = download_youtube_audio(video_url, download_folder)
    # print(f"Transcribing audio: {audio_file}")
    transcribed = transcribe_audio(audio_file)
    write_to_file(download_folder, 'transcribed.txt', transcribed)
    translated = translate('hindi', "all right we're gonna do it once more and this time no mistakes one two three four good morning good morning it's great to stay up late good morning good morning to you when the band began to play the skies were shining bright but now the milk man's on his way it's too late to say good night good morning good morning to you could be grander than to be in Louisiana in the morning in the month oh I'm sorry I thought we were still going")
    write_to_file(download_folder, 'translated.txt', translated)
    print('Done. Check folder ' + download_folder)
