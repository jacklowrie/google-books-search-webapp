

import requests

#get query from frontend

#parse query

#send to google books
search = requests.get("https://www.googleapis.com/books/v1/volumes?q='the+amulet+of+samarkand'")

#parse the results
results = search.json()

#format for frontend
#display
print(results)
