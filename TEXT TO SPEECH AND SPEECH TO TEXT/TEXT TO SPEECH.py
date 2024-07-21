import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")

def translate_speech():
    speech_recognizer = sr.Recognizer()
    language_translator = google_translator()

    with sr.Microphone() as source:
        print("SPEAK NOW !!!")
        audio = speech_recognizer.listen(source)

        try:
            speech_text = speech_recognizer.recognize_google(audio)
            print("Recognized Speech:", speech_text)
            return speech_text  # Return the recognized speech
        except sr.UnknownValueError:
            raise SpeechRecognitionError("COULDN'T UNDERSTAND !!!")
        except sr.RequestError:
            raise GoogleRequestError("COULD NOT REQUEST FROM GOOGLE !!!")

while True:
    print("\n---------------------------PROGRAM START--------------------------------------")
    print("\nTASK\n1. PRESS 1 if you want to convert voice message into a text message\n2. PRESS 2 if you want to convert text message into a voice message\n3. PRESS 3 to EXIT")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Converting voice message into a text message...")
        speech_text = translate_speech()
        if speech_text:
            print("Recognized text:", speech_text)
        else:
            print("Could not recognize speech.")
    elif choice == '2':
        print("Converting text message into a voice message...")
        input_lines = []

        print("Enter text (press Enter after each line; type 'done' to finish):")
        while True:
            line = input()
            if line.lower() == 'done':
                break  # Exit the loop if 'done' is entered
            input_lines.append(line)  # Append the input line to the list

        # Join the input lines into a single string, removing all newline characters
        input_text = "".join(input_lines)

        text = input_text.lower()  # Convert entered message to lowercase

        language = input(
            "\nCHOICE\n1. Hindi ascent \n2. English ascent\n3. French ascent\n4. Gujarati ascent\n\nENTER IN WHICH ASCENT YOU WANT TO PRONOUNCE YOUR TEXT :- ")
        if language == '1':
            langu = 'hi'
        elif language == '2':
            langu = 'en'
        elif language == '3':
            langu = 'fr'
        elif language == '4':
            langu = 'gu'
        else:
            print("ENTER CHOICE IS NOT A VALID CHOICE!!!!")
            continue  # Skip to the next iteration of the loop

        text_to_speech(text.replace('\n', ''),
                       langu)  # Remove newline characters and pass the text for speech synthesis
        print("TASK SUCCESSFULLY COMPLETED......\n")
    elif choice == '3':
        print("Exiting the program. Goodbye!\n")
        break  # Exit the while loop
    else:
        print("PLEASE ENTER A VALID CHOICE!!!!\n")
