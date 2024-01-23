
import pyttsx3
text_speech = pyttsx3.init()
print('Welcome to Text To Speech')
while True:
  user_text = input('enter text to want to change to speech: ')
  if user_text.lower() == 'q':
    text_speech.say("thanks for using")
    text_speech.runAndWait()
    break
  text_speech.say(user_text)
  text_speech.runAndWait()
  