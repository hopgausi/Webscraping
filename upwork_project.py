import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.mcexpocomfort.it/en/Exhibitor-Online-Directory/#search=d%3D103945%7C1111_109%26rpp%3D64'
page_content = requests.get(url)
soup = BeautifulSoup(page_content.content,'html.parser')
items = soup.find_all(class_='listItemDetail exhibitorDetail')
print(len(items))
names = [item.find(class_='name').get_text() for item in items]
hall = [item.find(class_='formSection attributeattribute-dataType-textboxonelineonelanguage attribute-Id-104603 attribute-Name-hall keyvaluepair').get_text() for item in items]
stand= [item.find(class_='formSection attributeattribute-dataType-textboxonelineonelanguage attribute-Id-104602 attribute-Name-stand keyvaluepair').get_text() for item in items]

company_detail = pd.DataFrame(
    {
        'Company Name':names,
        'Hall':hall,
        'Stand':stand,
    }
)
print(company_detail)
company_detail.to_csv('company.csv')
