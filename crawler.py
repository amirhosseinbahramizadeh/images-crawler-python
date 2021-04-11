import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("link site")
soup = BeautifulSoup(page.text, "html.parser")

temp = soup.select("img")
image_links = [image['src'] for image in temp]

for link in tqdm(image_links):
    file = requests.get(link)
    
    file_name = link.split('/')[-1]
    
    if '.' in file_name:
        file_type = '.' + file_name.split('.')[-1]
    else:
        file_type = '.jpg'
    
    file_address = 'Path directory' + str(image_links.index(link)) + file_type
    with open(file_address, 'wb') as f:
        f.write(file.content)