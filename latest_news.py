import requests

__api_key__ = "8e3c729034dd4967aee99f24182f9776"

def get_news(num_articles = 2):
    main_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + __api_key__
    news = requests.get(main_url).json()
    articles = news["articles"]

    news_articles = []

    for article in articles:
        if(num_articles == 0):
            break
        news_articles.append([article["title"], article["description"], article["url"]])
        num_articles -= 1

    return news_articles
