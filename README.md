🔊 VidSpeak – Text to Speech & YouTube Transcript Downloader
👋 Introduction

Reading long text content or manually writing notes from videos can be tiring and time-consuming. VidSpeak is a desktop application designed to solve this problem by allowing users to listen to text content and download transcripts from YouTube videos in document format.

This project is built using Python and Tkinter, integrating text-to-speech functionality and YouTube transcript extraction to assist users in their daily tasks such as studying, note-making, and content consumption.

🔍 Understanding the Problem

Many users face difficulties such as:

Eye strain from reading large amounts of text

Trouble making notes while watching educational videos

Lack of simple tools that combine listening and note generation

VidSpeak addresses these issues by converting text into audio and automatically generating notes from YouTube videos.

🔊 Text-to-Speech Feature

The Text-to-Speech module allows users to convert written text into spoken audio.

🧠 How It Works:

User enters the text they want to listen to.

The application uses Google Text-to-Speech (gTTS) to generate audio.

The audio is saved as an .mp3 file.

The generated file is played automatically.

✅ Benefits:

Helps users listen instead of reading

Useful for multitasking

Assists users with reading difficulties

📄 YouTube Transcript Downloader

The YouTube Transcript Downloader allows users to generate notes directly from YouTube videos.

🧠 How It Works:

User pastes a YouTube video link.

The application fetches the available transcript using YouTube’s caption data.

The transcript is saved as a .docx file.

The file can be used as study notes or documentation.

🖥️ Graphical User Interface

VidSpeak provides a simple and interactive GUI built using Tkinter.

🎨 Interface Features:

Text input fields

Buttons for listening and downloading

Menu bar with:

About section

History of saved audio files

Exit option

Alert messages for errors and confirmations

🧠 Technologies Used

🐍 Python 3.x

🖥️ Tkinter – GUI development

🖼️ Pillow (PIL) – Image handling

🔊 gTTS – Text-to-Speech conversion

▶️ playsound – Audio playback

📺 youtube-transcript-api – Transcript extraction

📄 python-docx – Word document creation

🧰 os, tkinter.messagebox – Utility modules

📌 Assumptions

To ensure smooth execution, the following assumptions are made:

User has an active internet connection.

Python 3.x is installed on the system.

Required Python libraries are properly installed.

The YouTube video has subtitles available.

The application has permission to save files locally.

✅ This project demonstrates the practical use of GUI development, API integration, and file handling to create a user-friendly desktop application that simplifies listening and note-making tasks.
