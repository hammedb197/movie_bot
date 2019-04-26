from flask import Flask, jsonify, render_template, request
import requests
import json
import os

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/get_movie_detail', methods=['POST'])
def get_movie_detail():
	data= request.get_json(silent=True)

	try:
		movie = data['queryResult']['parameters']['movie']
		api_key = os.getenv('OMDB_API_KEY')



		movie_detail = requests.get('http://www.omdbapi.com/?t={0}&apikey={1}'.format(movie, api_key)).content
		movie_detail = json.loads(movie_detail)

		response = '''
		Title: {0}
		Released : {1}
		Actors: {2}
		Plot: {3}'''.format(movie_detail['Title'], movie_detail['Released'], movie_detail['Actors'], movie_detail['Plot'])
	except:
		response = 'Movie id not avsilabe'
	


	reply = {'fulfilment': response}
	return jsonify(reply)


if __name__=='__main__':
	app.run()