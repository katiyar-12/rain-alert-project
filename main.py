import requests
from aiohttp.log import client_logger
from pyexpat.errors import messages

from twilio.rest import Client




acount_sid = "AC8493d99ff89ad5c601385fae9218ce4f"
auth_token = "8ae04af2ad11db316032ab5a73fbdea3"


api_key = "da2db07b20ddadfb35eaa17c19f15f15"


longitude = 78.962883
latitude = 20.593683




parameters = {
    "lat" : latitude ,
    "lon" : longitude ,
    "appid" : api_key ,
    "cnt" : 4 ,
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()

weather_data = response.json()["list"][0]["weather"][0]["id"]

condition_codes = []
will_send = False
for index in range(parameters["cnt"]) :
    condition_codes.append(response.json()["list"][index]["weather"][0]["id"])



for choice in condition_codes :
    if choice < 700 :
        will_send = True

if will_send :
    client = Client(acount_sid,auth_token)
    message = client.messages.create(from_="+18564394300", to="+918955209025",body="=Bring an umbrella there will be rain today")

