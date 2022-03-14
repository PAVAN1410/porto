# porto
PORTO is basically a portfolio generating website.

Flow of the data in PORTO:

From the frontend home page we take the linkedIn profile link that is to be scraped and make a
portfolio. This link is passed to linkedin_scraper.py file where we initiate a testing browser for
automation of the linkedIn profile using selenium and chrome driver. Initially we login to linkedIn
website by using selenium. Now we use the link provided by the user and load their profile on the
test browser. Now we click all the see more buttons on the profile for loading the entire website.
Taking beautiful soup tool to full advantage we parse the HTML through soup and make it as a
soup readable format. By using this soup we will scrap required data from website by using class
names, ids and the element type(eg. Div, button, forms,....). Now we convert entire data to JSON
format.
All the JSON data will be stored in the static folder. Next step is to place all the data into the
templates we created. For this we use the FETCH function for getting the data from the JSON file
which is in a static folder. Now we use a call back function after executing the fetch and extract
data from the JSON file. Now we use javascript for dynamic creation of elements and add the data
to these elements and place this data on the HTML DOM. We used the zipFile function to zip all
the files that are required to host the website and provide those files to the user.
