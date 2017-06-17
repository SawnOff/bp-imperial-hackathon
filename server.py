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
