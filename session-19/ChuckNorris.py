import http.client
import json


def gettinginfo(HOSTNAME,ENDPOINT, METHOD):


    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection(HOSTNAME)

    conn.request(METHOD, ENDPOINT, None, headers)

    r1 = conn.getresponse()

    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    text_json = r1.read().decode("utf-8")
    conn.close()


    # -- Generate the object from the json file
    cat = json.loads(text_json)
    return cat


randomjoke = gettinginfo("api.icndb.com", "/jokes/random", "GET")

print("This is the random joke: ", randomjoke['value'])

category = gettinginfo("api.icndb.com", "/categories", "GET")

print("Here are the categories: ", category['value'])

count = gettinginfo("api.icndb.com", "/jokes/count", "GET")

print("The total number of jokes: ", count['value'])