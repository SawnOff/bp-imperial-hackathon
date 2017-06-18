import numpy as np
import cv2
from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    return question("Welcome to BP Report.")

@ask.intent('Best')
def best():
    speech_text = "Rishi is the best"
    return statement(speech_text).simple_card('Hi', speech_text)

@ask.intent('AMAZON.HelpIntent')
def help():
    return question("Please say something HELP")

@ask.intent('WeatherIntent', mapping={'city': 'City'})
def weather(city):
    return statement('I predict great weather for {}'.format(city))

@ask.intent('AddIntent', convert={'x': int, 'y': int})
def add(x, y):
    z = x + y
    return statement('{} plus {} equals {}'.format(x, y, z))

@ask.intent('Show')
def show():
    return statement("show")
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not cap.isOpened(): print('Can\'t open cap')
        if frame.empty(): break

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return statement('Camera session ended')

#REPLACE WITH PUSH NOTIFICATIONS
@ask.intent('SmokeWarn')
def warn():
    return statement('No smoking allowed in this area')

@ask.intent('Update')
def update(loc):
    print("Location: {}".format(loc))
    #no = number of petrol station users
    if loc == 'station':
        pumpstatus = [False, True, False, True, False]

        #sm = number of smokers
        occpumps = "".join(["Pump {} {} occupied. ".format(i + 1, "" if val else "not") for (i, val) in enumerate(pumpstatus)])

        return statement(occpumps)

    if loc == 'pump':
        occ = True
        if occ:
            return statement('<speak>That  <prosody volume="x-loud">pump</prosody> is occupied</speak>')
        else:
            return statement("That pump is vacant")
          
    return statement("I don't know about this location")

#REPLACE WITH PUSH NOTIFICATIONS

@ask.intent('AgeIntent', convert={'age': int})
def say_age(age):
    if 'age' in convert_errors:
        # since age failed to convert, it keeps its string
        # value (e.g. "?") for later interrogation.
        return question("Can you please repeat your age?")

    # conversion guaranteed to have succeeded
    # age is an int
    return statement("Your age is {}".format(age))

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return question("Please say something CANCEL")

@ask.intent('AMAZON.StopIntent')
def stop():
    return question("Please say something STOP")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
