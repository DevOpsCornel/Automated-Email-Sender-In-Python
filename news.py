import requests

class NewsFeed:
    """Representing multiple news tit;e and links as a single string"""

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "1a7dbc49a8e2468db378a4894ab94fdf"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self.extract_url()

        articles = self.get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        print(content)
        articles = content['articles']
        return articles

    def extract_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


news_feed = NewsFeed(interest='nasa', from_date='2023-08-25', to_date='2023-08-30', language='en')
print(news_feed.get())
