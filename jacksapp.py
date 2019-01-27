

import requests

#get query from frontend
    #...code goes here
#parse query
    #...code goes here
#construct the GET request
parameters = {'q' : 'amulet+of+samarkand', 'projection' : 'lite'}

#send to google books
search = requests.get('https://www.googleapis.com/books/v1/volumes', params=parameters)

#parse the results
results = search.json()

#format for frontend
#display
print(results)
