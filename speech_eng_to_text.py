'''import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))'''


class Speech_to_text:

    def gettext(self):
        txt = "ntng"
        success = False
        try:
            import speech_recognition as sr

            success = True
            txt = "1st rnd"

        except ImportError:
            txt = "Please Install Speech Recognition Module via pip or any other Source"


        if success:
            r = sr.Recognizer()
            success = False
            try:
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = r.listen(source)
                    txt = "2nd rnd"
                    success = True


            except sr.UnknownValueError:
                txt = "Unable to find default device, Please update pyaudio"
            except sr.RequestError as e:
                txt = "Could not request results from Google Speech Recognition service; {0}".format(e)


            if success:
                success = False
                try:
                    txt = r.recognize_google(audio)
                    success = True
                except sr.UnknownValueError:
                    txt = "Google Speech Recognition could not understand audio"
                except sr.RequestError as e:
                    txt = "Could not request results from Google Speech Recognition service; {0}".format(e)

        return success, txt
