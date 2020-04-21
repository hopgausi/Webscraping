import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
url_content = requests.get(url)
#print(url_content.status_code)
html_source_content = url_content.content
#print(html_source_content)
soup = BeautifulSoup(html_source_content,'html.parser')

required_content_to_scrape = soup.find_all('a',{'class':'_31qSD5'})
filename = 'mobile_product.csv'
f = open(filename,'w')
title = 'PRODUCT_NAME, SPECS DETAILS, PRICE(MWK), RATINGS\n'
f.write(title)

for content in required_content_to_scrape:
    product_name = content.find_all('div',{'class':'_3wU53n'})
    name = product_name[0].text.replace(',','|')
    #print(name)

    details = content.find_all('div',{'class':'_3ULzGw'})
    specs = details[0].text.replace(',','|')
    #print(specs)

    product_price = content.find_all('div',{'class':'_1vC4OE _2rQ-NK'})
    price = product_price[0].text
    to_malawi_kwacha = 10.23
    price = int(''.join(price.split(',')).encode('ascii', 'ignore')) * to_malawi_kwacha
    #print(price)

    product_rating = content.find_all('div', {'class': 'hGSR34'})
    rating = product_rating[0].text
    #print(rating)
    final_result  = name+','+specs+','+str(price)+','+rating+'\n'
    f.write(final_result)


f.close()
