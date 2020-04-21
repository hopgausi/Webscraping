import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://itsfoss.com/all-blog-posts/'
page_content = requests.get(url)
#print(page_content)

html_page_source = page_content.content

#create a BeatifulSoup object
soup = BeautifulSoup(html_page_source,'html.parser')
#print(soup.prettify())

content = soup.find(id='genesis-content')
#print(content)

#get a list of articles
blogposts = content.find_all('article')
#print(blogposts)

#get a list of titles with tags
blog_title = [(blog.find_all(class_='entry-title-link'))  for blog in blogposts]

#get a list of authors with tags
blog_author = [(blog.find_all(class_='entry-author-name'))  for blog in blogposts]

#get a list of dates with tags
date = [(blog.find_all(class_='entry-modified-time'))  for blog in blogposts]

#get a list of descriptions with tags
blog_sum = [(blog.find_all(class_='entry-content'))  for blog in blogposts]

#get a list of all titles text
title = []
for item in blog_title:
    heading = item[0].get_text().encode('ascii','ignore')
    title.append(heading)
#print(title)

#get a list of all athors names
author_= []
for item in blog_author:
    author = item[0].get_text().encode('ascii','ignore')
    author_.append(author)
#print(author_)

#get a list of all dates
update_date= []
for item in date:
    date_item = item[0].get_text().encode('ascii','ignore')
    update_date.append(date_item)
#print(update_date)


#get a list of all descrpitons
summ= []
for item in blog_sum:
    heading = item[0].get_text().encode('ascii','ignore')
    summ.append(heading)
#print(summ)

# Translate into row * column data via pandas
itsfoss = pd.DataFrame({
    "AUTHOR": author_,
    "LAST UPDATED": update_date,
    "ARTICLE TITLE" : title,
    "OPENING SUMMARY TEXT" : summ,
})
#print(itsfoss)

# store data into csv file
itsfoss.to_csv('itfoss_articles.csv', index=False)