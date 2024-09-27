import os
import requests
from back_end.views import weather_views
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()

@weather_views.route('/current', methods=['GET'])
def get_current_weather():
    """Gets the current weather details"""
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({'error': 'Missing latitude or longitude'}), 400
    API_KEY = os.getenv('OPENWEATHER_MAP_API_KEY')

    if not API_KEY:
        # use a placeholder temperature
        """if (response.ok && info.data && info.data.main) {	
					setTemperature(info.data.main.temp);
					setIcon(info.data.weather[0].icon)
				} else {
					setError(info.message);
				}
        """ # DEBUG
        return jsonify({
            'data': {
                'main': {'temp': 25.0}
            }
            }), 200

    url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}'
    try:
        response = requests.get(url)
        info = response.json()
        print('returning weather', info) # DEBUG
        return jsonify({
            'data': info
        }), 200
    except requests.RequestException as e:
        return jsonify({
            'error': 'Could not get weather at this time'
        }), 500
