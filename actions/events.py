import requests

def event():
    URL_api_address='http://127.0.0.1:8000/api/events/2'
    json_data= requests.get(URL_api_address).json()
    print( json_data)
    return json_data