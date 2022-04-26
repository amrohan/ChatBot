import os
import json
import datetime
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# we use this to get api key from env files
load_dotenv()
Dev_Token = os.getenv('Dev_Token')

'''
💡Use this version if you deploying it on repl.it
# Getiing bot token from env file
Dev_Token = os.environ['Dev_Token']

'''


# Getting TLDR articales
def currentDate():
    date = datetime.datetime.now()
    date = date.strftime("%Y-%m-%d")
    return date

# Scrapping data from tldr page


def tldrData():
    date = datetime.datetime.now()
    date = date.strftime("%Y-%m-%d")
    url = 'https://tldr.tech/newsletter/' + date
    print(url+"\nSending Data...")
    response = requests.get(url)
    # check response status
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
    # find all div tag with class mt-3
        divs = soup.find_all('div', class_='mt-3')
        for content in divs:
            rawData = content.text.strip()
            # clear new line from data
            data = rawData.replace('\n\n', '')
            # Taking out only Programming, Design & Data Science section
            mainData = data.split('\n')[16: 24]
            # joininng all data into one string
            joinData = '\n'.join(mainData)
            # add new line to joindata after 5 index
            finalData = joinData.replace('\n', '\n\n', 5)
            # add new line to finalData
            article = finalData + '\n' + "Read full article at: " + url
            print("TLDR Sent Succesfully 🚀")
            return (article)
    else:
        print("No articles today")
        return ("Sorry, on "+date+" there is no new article on tldr.tech ☹️")


# Getting Dev To articles:
def devto():
    url = "https://dev.to/api/articles/"
    res = requests.get(url, headers={"Api-Key": Dev_Token})
    data = res.json()

    title = data[0].get("title")
    desc = data[0].get("description")
    url = data[0].get("url")

    title1 = data[1].get("title")
    desc1 = data[1].get("description")
    url1 = data[1].get("url")

    title2 = data[2].get("title")
    desc2 = data[2].get("description")
    url2 = data[2].get("url")

    title3 = data[3].get("title")
    desc3 = data[3].get("description")
    url3 = data[3].get("url")

    title4 = data[4].get("title")
    desc4 = data[4].get("description")
    url4 = data[4].get("url")

    title5 = data[5].get("title")
    desc5 = data[5].get("description")
    url5 = data[5].get("url")

    finalData = 'Dev.to Top Article 🧑‍💻\n'+'\n'+'Article : '+title+'\n\n' + \
        'Description : '+desc+'\n\n'+'Read Full article at : '+url+'\n\n' +\
        '--------x--------'+'\n\n'+'Article_01 : '+title1+'\n\n' + \
        'Description : '+desc1+'\n\n'+'Read Full article at : '+url1+'\n\n'\
        '--------x--------'+'\n\n'+'Article_02 : '+title2+'\n\n' + \
        'Description : '+desc2+'\n\n'+'Read Full article at : '+url2+'\n\n'\
        '--------x--------'+'\n\n'+'Article_03 : '+title3+'\n\n' + \
        'Description : '+desc3+'\n\n'+'Read Full article at : '+url3+'\n\n'\
        '--------x--------'+'\n\n'+'Article_04 : '+title4+'\n\n' + \
        'Description : '+desc4+'\n\n'+'Read Full article at : '+url4+'\n\n'\
        '--------x--------'+'\n\n'+'Article_05 : '+title5+'\n\n' + \
        'Description : '+desc5+'\n\n'+'Read Full article at : '+url5+'\n\n'

    print('Devto Sent Succesfully 🚀')

    return finalData


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']+"\n - by "+json_data[0]['a']
    print('Quotes Sent Succesfully 🚀')
    return (quote)
