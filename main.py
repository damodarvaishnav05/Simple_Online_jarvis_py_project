
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Here we define a function to open the demonstration of various platforms
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")

    elif "open gemini" in c.lower():
        webbrowser.open("https://www.google.com/aclk?sa=L&ai=DChsSEwjtkpaY8cOPAxVF9TwCHW4QIT8YACICCAEQABoCc2Y&ae=2&co=1&ase=2&gclid=CjwKCAjwt-" \
                        "_FBhBzEiwA7QEqyOfEVVdzQNIkSSsB0aVaxKve00m7BD85POKuhc9Dv2D8xyU0-w6GEhoCl4MQAvD_BwE&cce=2&category=acrcp_v1_71&sig=AOD64_1jsLFy23LEJXurWVo9" \
                        "WtvTj2JkLQ&q&nis=4&adurl&ved=2ahUKEwim2I6Y8cOPAxUNfGwGHUV2FFAQ0Qx6BAgLEAE")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    else:  # Here we use the open ai will handle the other all stuff
        pass



if __name__ =="__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listening for the wake word
        r = sr.Recognizer()


        # recognize speech using google
        print("Recognizing...")

        try:  
            # The try is because u dont need to worry about the error 
            # because the code will be seperated by errors                               
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes")

                # Here listen for commands
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)



        except Exception as e:
            print("Error; {0}".format(e))



