from bs4 import BeautifulSoup
import requests
import csv

url = 'https://coreyms.com/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('corey.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['Headline', 'Summary', 'Youtube link'])


for article in soup.find_all('article'):
    try:
        headline = article.find('a', class_='entry-title-link').get_text()
        summary = article.find('div', class_='entry-content').p.get_text()

        video_link = article.find('iframe', class_='youtube-player')['src']
        video_id = video_link.split('/')[4].split('?')[0]
        youtube_link = f'https://www.youtube.com/watch?v={video_id}'

    except:
        pass

    writer.writerow([headline,summary,youtube_link])

csv_file.close()
