import speech_recognition as sr
class VoiceModule():
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.input = sr.Microphone()



    # Capture audio from the microphone
    def listen(self):
        with self.input as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            return audio

    # Save audio file
    def save(self, audio):
        return

    #Convert audio to string
    def recognize(self, audio):
        text = ''
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")

        except sr.UnknownValueError:
            print("Sorry, I could not understand your audio.")
        except sr.RequestError as e:
            print(f"Sorry, an error occurred: {str(e)}")
        
        return text

vm = VoiceModule()
audio = vm.listen()
vm.recognize(audio)