#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
#MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get('http://api.open-notify.org/astros.json').json()
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()


    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    
    
    #helmetson = groundctrl.json()


    ## display our Pythonic data
    #print("\n\nConverted Python data")
    #print(helmetson)
    print(f"Number in space: {groundctrl['number']}")
    for x in groundctrl["people"]:
        print(f"{x['name']} is on the {x['craft']}.")

    #print('\n\nPeople in Space: ', helmetson['number'])
    #people = helmetson['people']
    #print('\n', helmeston['people']['name'], 'is on the ', helmeston['people']['craft'])

if __name__ == "__main__":
    main()

