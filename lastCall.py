#################

import requests
import json

##### Variables to define. Input the apiKey to use and the username to look up #####

apiKey = ''
userAgent = 'paulymusic'


# Function to get the response from Last.fm

def lastGetResponse(payload,getUser,getLimit):
    # define headers and URL
    headers = {'user-agent': userAgent}
    url = 'https://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload['api_key'] = apiKey
    payload['format'] = 'json'
    payload['user'] = getUser
    payload['limit'] = getLimit

    response = requests.get(url, headers=headers, params=payload)
    return response

# Function using jprint to show the results of JSON

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def setValuesCall(inmethodA,inmethodB,inUser, inLimit):

    callResponse = lastGetResponse({inmethodA : inmethodB},inUser,inLimit)

    return callResponse

