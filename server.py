from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    return question("Say hello")

@ask.intent('Hello')
def hello(name):
    speech_text = "Nice to meet you, {}".format(name)
    return statement(speech_text).simple_card('Hi', speech_text)

@ask.intent('AMAZON.HelpIntent')
def help():
    return question("Please say something HELP")

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return question("Please say something CANCEL")

@ask.intent('AMAZON.StopIntent')
def stop():
    return question("Please say something STOP")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
