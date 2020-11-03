#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    groundctrl = urllib.request.urlopen(MAJORTOM)
    helmet = groundctrl.read()
    helmetson = json.loads(helmet.decode('utf-8'))
    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    for x in people:
        print(x["name"])

if __name__ == "__main__":
    main()
