import requests


url ='http://api.openweathermap.org/data/2.5/weather?q=Seattle,USA&units=imperial&APPID=6d35bfb76b49dd76492408f6ac791e48'
response =  requests.get(url)
weather_json =  response.json()
feels_like = weather_json.get('main').get('feels_like')
temp = weather_json.get('main').get('temp')
temp_max = weather_json.get('main').get('temp_max')
temp_min = weather_json.get('main').get('temp_min')
current_weather = weather_json.get('weather')[0].get('description')


print(f"Today in Seattle it feels like {feels_like} degrees with  {current_weather}")
print(f'The high today will be {temp_max} and a low of {temp_min}')