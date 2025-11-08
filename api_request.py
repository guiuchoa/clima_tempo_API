import requests

api_key = "8a40287796f1ee0fe20157871ea50337"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=Nova Iguacu"

# def fetch_data():
#     print("Puxando dados de tempo/clima da API do WeatherStack...")
#     try:

#         response = requests.get(api_url)
#         response.raise_for_status()
#         print("Resposta da API retornou com sucesso")
        
#         return response.json()

#     except requests.exceptions.RequestException as e:

#         print(f"Ocorreu um erro: {e}")
#         raise

# fetch_data()


# Função para não ficar chamando o tempo todo a API
def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Nova Iguacu, Brazil', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Nova Iguacu', 'country': 'Brazil', 'region': 'Rio de Janeiro', 'lat': '-22.757', 'lon': '-43.449', 'timezone_id': 'America/Sao_Paulo', 'localtime': '2025-06-28 11:44', 'localtime_epoch': 1751111040, 'utc_offset': '-3.0'}, 'current': {'observation_time': '02:44 PM', 'temperature': 26, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly Cloudy '], 'astro': {'sunrise': '06:34 AM', 'sunset': '05:20 PM', 'moonrise': '09:21 AM', 'moonset': '08:43 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 8}, 'air_quality': {'co': '597.55', 'no2': '36.63', 'o3': '183', 'so2': '17.39', 'pm2_5': '83.805', 'pm10': '87.69', 'us-epa-index': '4', 'gb-defra-index': '4'}, 'wind_speed': 8, 'wind_degree': 94, 'wind_dir': 'E', 'pressure': 1022, 'precip': 0, 'humidity': 65, 'cloudcover': 25, 'feelslike': 27, 'uv_index': 5, 'visibility': 10, 'is_day': 'yes'}}