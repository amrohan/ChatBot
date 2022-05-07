from mega import Mega
import os
import schedule
import time
from scraper import get_hackerNews, get_techcrunch, get_tldr
from dotenv import load_dotenv

# we use this to get api key from env files
load_dotenv() 
email = os.getenv('email')
passWord = os.getenv('pass')


mega = Mega()

m = mega.login(email, passWord)

details = m.get_user()


def uploadAll():

    # uploading all files to dropbox also storaing data
    tldr1, tldr2, tldr3, tldr4 = get_tldr()
    tldrData = tldr1+tldr2+tldr3+tldr4
    with open('./Files/tldr.txt', 'w', encoding='utf-8') as f:
        f.write(tldrData)
        f.close()

    # Hacker News
    hackerNewsTop, hackerNewsMore = get_hackerNews()
    hackerNewsData = hackerNewsTop + '\n' + hackerNewsMore

    with open('./Files/hackernews.txt', 'w', encoding='utf-8') as f:
        f.write(hackerNewsData)
        f.close()

    # TechCrunch
    techcrunchArticles, furtherArticles, lastArticles = get_techcrunch()
    techData = techcrunchArticles+furtherArticles+lastArticles

    with open('./Files/techcrunch.txt', 'w', encoding='utf-8') as f:
        f.write(techData)
        f.close()

    # finding folder in mega
    folder = m.find('scrapeData')
    m.upload('./Files/tldr.txt', folder[0])
    m.upload('./Files/techcrunch.txt', folder[0])
    m.upload('./Files/hackernews.txt', folder[0])
    print('All files are uploaded')


def timeUpload():
    schedule.every().day.at("11:00").do(uploadAll)
    while True:
        schedule.run_pending()
        time.sleep(20)
        print('I am running')
