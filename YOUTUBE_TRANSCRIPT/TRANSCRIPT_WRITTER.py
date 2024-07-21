print("PROJECT START")
from youtube_transcript_api import YouTubeTranscriptApi
import os

video_link = input("Enter the YouTube video link: ")

filename = input("Enter the name for the text file (without extension): ") + ".txt"

try:

    srt = YouTubeTranscriptApi.get_transcript(video_link)

    with open(filename, "w") as file:
        for i in srt:
            print(i)
            text = i["text"] + ", "
            file.write(text)

    os.rename(filename,filename)
    print("Transcript saved successfully as VEDIO_NOTES.txt")

except Exception as e:
    print("Error:", e)
