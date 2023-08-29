"""Import all the necessary packages, kindly use google to determmine what you want to do"""
import datetime as datetime
import yagmail
import pandas
import yagmail as yagmail

from news import NewsFeed
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today)
    email = yagmail.SMTP(user="huboftech1@gmail.com", password="dibuqilcxgxuvojk")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what is on about {row['interest']} today. {news_feed.get()} \nTunji", )


while True:
    if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 35:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)
