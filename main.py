from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
import schedule 
import time

import bot_intents_creation

from bot_creation import chatbot_response
from bot_creation import create_bot_model

import utils

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#@app.route('/api/v1/createBotModel', methods=["GET"])
#@cross_origin()
def create_bot_model():

    bot_intents_creation.create_all_intents_and_save()
    create_bot_model()
    return "true"


@app.route('/api/v1/botResponse', methods=["GET"])
@cross_origin()
def bot():

    input = request.args.get("input")
    input = utils.adapt_phrase_to_bot(input)

    response_from_chatbot = chatbot_response(input)
    flask_response = {"response": response_from_chatbot}

    return jsonify(flask_response)

schedule.every(24).hours.do(create_bot_model)

app.run(debug=False, host="0.0.0.0")

while True:
    schedule.run_pending()
    time.sleep(1)