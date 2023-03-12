import datetime
import webbrowser as wb

import bs4
import pyjokes as pyj
import requests


def wish_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        return "Good Morning, How can I help you?"
    elif hour >= 12 and hour < 18:
        return "Good Afternoon, How can I help you?"  
    else:
        return "Good Evening, How can I help you?"

def open_youtube(query = None):

    youtube_url = "http://www.youtube.com"
    if query is None:
        wb.open(youtube_url)
    else:
        wb.open(youtube_url + f"/results?search_query={query}")

def open_google(query = None):

    google_url = "http://www.google.com"
    if query is None:
        wb.open(google_url)
    else:
        search_query = str(query).split("search google for ")[-1].strip()

        res = requests.get(f'https://google.com/search?q={search_query}')
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        search_results = soup.select('.kCrYT a')

        if not search_results:
            return "No search results found."
        else:
            first_result = search_results[0].get('href')
            wb.open(f"https://google.com{first_result}")

def get_joke():
    return pyj.get_joke()
