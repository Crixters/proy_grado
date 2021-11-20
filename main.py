from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

import bot_intents_creation

from bot_creation import chatbot_response
from bot_creation import create_bot_model

import utils

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

bot_intents_creation.create_all_intents_and_save()
create_bot_model()

@app.route('/api/v1/botResponse',methods=["GET"])
@cross_origin()
def bot():

    input = request.args.get("input")
    input = utils.adapt_phrase_to_bot(input)
    
    response_from_chatbot = chatbot_response(input)
    flask_response = { "response":response_from_chatbot }

    return jsonify(flask_response)

app.run(debug=True)
