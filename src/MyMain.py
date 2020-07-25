import requests
from bs4 import BeautifulSoup
from csv import writer
import datetime

response = requests.get('https://www.foxnews.com/')

soup = BeautifulSoup(response.text,features="html.parser")# features for error in virtual enviroment

name={'Fox News'}
link = {'<a>https://www.foxnews.com/</a>'}

lines = soup.find_all(class_='info-header')

with open('posts.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['title']
    csv_writer.writerow(headers)

    #time
    time = datetime.datetime.now()
    csv_writer.writerow('Date: ')
    currentTime = time.strftime("%x")
    csv_writer.writerow(currentTime)

    titles =[]
    for line in lines:

        title = line.find(class_='title').get_text()

        titles.append(title)


    csv_writer.writerow(titles)

