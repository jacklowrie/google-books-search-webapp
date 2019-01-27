

import requests #this thing is awesome

#get query from frontend
    #...code goes here
#parse query
    #...code goes here
#construct the GET request
hp = 'harry potter sorcerer\'s stone' #test search many results
quarterboys = 'intitle:reckoning+inauthor:david+inauthor:lennon' #test search one result
noresults = '3ugn398' #test search no results
parameters = {'q' : noresults, 'projection' : 'lite'}

#send to google books
search = requests.get('https://www.googleapis.com/books/v1/volumes', params=parameters)

#parse the results
results = search.json()

#format for frontend display
print('number of results: ' + str(results.get("totalItems")) + '\n\n\n')
print(search.url + '\n\n\n')
print(str(search.status_code) + '\n\n\n')
print(results)
