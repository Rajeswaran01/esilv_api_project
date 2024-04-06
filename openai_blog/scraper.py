import requests
from bs4 import BeautifulSoup

 

def fetch_articles(url):
    """
    Fetches articles from the given URL and parses them into a list of dictionaries.

 

    :param url: The URL to scrape articles from.
    :return: A list of dictionaries, each representing an article with title, URL, image URL, and date.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

 

        articles = []
        for li in soup.select('ul.cols-container li'):
            articles.append({
                'title': li.h3.text if li.h3 else 'No title',
                'url': li.a['href'] if li.a else 'No URL',
                'image_url': li.find('img')['src'] if li.find('img') else 'No image URL',
                'date': li.find('div', class_='f-body-1').span.text if li.find('div', class_='f-body-1') else 'No date'
            })

 

        return articles
    except Exception as e:
        print(f'Error fetching articles: {e}')
        return []
