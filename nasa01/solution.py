#!/usr/bin/env python3
import requests
from pprint import pprint as pp
NASAAPI = 'https://api.nasa.gov/planetary/apod?'
MYKEY = 'api_key=7s6TgHPkMGoIwAqRHeS0JrWzQ7UsGa6lS6caE59k'
DATE= "date=" + input("Enter the date you'd like to view in YYYY-MM-DD format. Otherwise press enter to accept today's date.")
HD= input("If you'd like your picture to be in HD, type hd=True. Otherwise hit enter to accept SD.")
def main(NASAAPI, MYKEY, DATE="date=2020-10-03", HD="hd=False"):
    nasaapiobj = requests.get(NASAAPI + DATE + "&" + HD  + "&" + MYKEY)
    # https://api.nasa.gov/planetary/apod?date=2017-01-03&hd=True&api_key=7s6TgHPkMGoIwAqRHeS0JrWzQ7UsGa6lS6caE59k
    nasaread = nasaapiobj.json()
    print(f"Title: {nasaread['title']}")
    print(f"Date: {nasaread['date']}")
    print(f"Explanation: {nasaread['explanation']}")
main(NASAAPI, MYKEY, DATE, HD)
