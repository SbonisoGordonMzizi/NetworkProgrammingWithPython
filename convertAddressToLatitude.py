#!/usr/bin/env python3
"""
this script is used to convert physical address to latitude and longitude
Note that!! You must use an API key to authenticate each request to Google Maps Platform APIs.    
"""
import requests

def geocode(address):
    parameters = {'address':address,'sensor':'false'}
   
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    responce = requests.get(base,params=parameters)
    answer = responce.json()
    if answer:
        #print(answer['results'][0]['geometry']['location'])
        print(answer)
    else:
        print("address not found")

if __name__ == '__main__':
    address = '84 Albertina Sisulu Rd, Johannesburg, 2000'
    geocode(address)