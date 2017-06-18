import numpy as np
import cv2
from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

please_text = "<speak>please <emphasis level=\"reduced\">please</emphasis> <emphasis level=\"moderate\">please</emphasis> <emphasis level=\"strong\">please</emphasis></speak>"

@ask.launch
def launch():
    return question("Say hello").reprompt(please_text)

@ask.intent('Hello')
def hello(name):
    speech_text = "Nice to meet you, {}".format(name)
    return statement(speech_text).simple_card('Hi', speech_text)

@ask.intent('AMAZON.HelpIntent')
def help():
    return question(please_text)

@ask.intent('WeatherIntent', mapping={'city': 'City'})
def weather(city):
    return statement('I predict great weather for {}'.format(city))

@ask.intent('AddIntent', convert={'x': int, 'y': int})
def add(x, y):
    z = x + y
    return statement('{} plus {} equals {}'.format(x, y, z))

@ask.intent('Show')
def show():
    cap = cv2.VideoCapture(0)

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
return statement('Camera session ended')

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Cancelled")

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Stopped")

@ask.session_ended
def session_ended():
    return statement("Bye bye lol")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
