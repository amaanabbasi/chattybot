import flask
from flask_restful import Resource, Api
from chatterbot import ChatBot

app = flask.Flask(__name__)
api = Api(app)
chatbot = None

def load_chatbot():
	''' Á function that loads the chatbot model '''
	global chatbot
	chatbot = ChatBot('Amaan')

class HelloWorld(Resource):
	def get(self, text):
		''' A api function that gets the input text and returns a reply
		in the form of a json object. '''

		print(text)
		response = chatbot.get_response(text)
		data = {text : str(response)}
		print(data)
		return data 

api.add_resource(HelloWorld,'/<string:text>')

if __name__ == '__main__':

	load_chatbot()
	app.run(debug=True)