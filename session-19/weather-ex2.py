import http.client
import json


HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query="
inputname = input('Enter a capital: ')
ENDPOINT += inputname

METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()


weather = json.loads(text_json)
LOCATION_WOEID = str(weather[0]['woeid'])

# ---------------------

ENDPOINT2 = "/api/location/"

headers = {'User-Agent': 'http-client'}

conn2 = http.client.HTTPSConnection(HOSTNAME)

conn2.request(METHOD, ENDPOINT2 + LOCATION_WOEID + '/', None, headers)

r2 = conn2.getresponse()

print()
print("Response received: ", end='')
print(r2.status, r2.reason)

text_json2 = r2.read().decode("utf-8")
conn2.close()

weather = json.loads(text_json2)


time = weather['time']
temperature = weather['the_temp']
sun_set = weather['sun_set']

print("This is the time: ", time)
print("This is the temperature: ", temperature)
print("This is the sun set: ", sun_set)