from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('HelloIntent')
def hello(firstname):
    speech_text = "Hello %s" % firstname
    return statement(speech_text).simple_card('Hello', speech_text)

if __name__ == '__main__':
    context = ('cert/server.crt', 'cert/server.key')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True,
            debug=True)
