# google books search webapp

This is a simple Python app that takes in a search query and then returns a list of results from the google books api. Each result includes the title (and subtitle if applicable), author(s), and publisher. It also provides a link to view each result on GoodReads.com. It was built primarily using Flask and the requests library.

### Next Steps
I plan to add pagination -- currently, each request to the google books api only returns 10 results, and can only return up to 40 results. I plan to add forward and backwards buttons that allow new requests to be sent for the same query, that way the user can navigate through the entire list of results.

I'd also like to make the app more visually appealing. It's currently very barebones on html and css.
