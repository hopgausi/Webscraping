from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

# grab the page contents
url = 'https://fountainsland.com/land-for-sale/?selection=NH,VT,available'
page_content = requests.get(url)
page_content_html_source = page_content.content

# beautifulsoup object, required information to be scraped
soup = BeautifulSoup(page_content_html_source, 'html.parser')
content_required = soup.find('div', class_='list')
content_required_items = content_required.find_all('div', class_='item')

try:
    # specific information source list in list
    name_items = [item.find_all('div', class_='name') for item in content_required_items]
    location_items = [item.find_all('div', class_='location') for item in content_required_items]
    price_acres_items = [item.find_all('div', class_='subinfo') for item in content_required_items]
    description_items = [item.find_all('div', class_='description') for item in content_required_items]
    website_items = [item.find_all('a') for item in content_required_items]

    # specific information items text list
    name = [item[0].get_text() for item in name_items]
    location = [item[0].get_text() for item in location_items]
    price_acres = [item[0].get_text().strip().split(":") for item in price_acres_items]
    description = [item[0].get_text() for item in description_items]
    websites = [item[0]['href'] for item in website_items]

    # getting price and acres
    acres = [acre[0].strip(' ACRES') for acre in price_acres]
    price = [price[1].strip(' $') for price in price_acres]

    # creating viable link
    website = [f'https://fountainsland.com/{website}' for website in websites]
except:
    pass



# create fountains_land pandas data frame (i.e table)
fountains_land = pd.DataFrame(
    {
        'Name': name,
        'Location': location,
        'Acres': acres,
        'Price $': price,
        'Description': description,
        'Website': website,
    }
)
# translate frame to csv name FountainLands.csv
fountains_land.to_csv('FountainLands.csv', index=False)
