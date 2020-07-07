# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 06:52:26 2019



@author: Sween
"""

from requests import get
from bs4 import BeautifulSoup

# INPUTS
#url = 'https://www.hotstar.com/channels/starplus'
#url = 'https://api.hotstar.com/o/v1/channel/detail?id=3&avsCategoryId=745&contentId=821&offset=0&size=20&pageNo=1&perPage=40'
url = 'https://api.hotstar.com/o/v1/channel/detail?id=3&avsCategoryId=745&contentId=821&offset=0&size=20&pageNo=1&perPage=40'
#url = 'https://api.hotstar.com/o/v1/channel/asset?id=3&offset=20&size=20&pageNo=1&perPage=20'

# Request headers
headers = {
        ':authority': 'api.hotstar.com',
        ':method': 'GET',
        ':path': '/o/v1/channel/detail?id=3&avsCategoryId=745&contentId=821&offset=0&size=20&pageNo=1&perPage=40',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'hotstarauth': 'st=1548930348~exp=1548936348~acl=/*~hmac=e20e60873914dcf8974bd1fa4d6a75502ac2f09bed0f6b321194cb55ba99e921',
        'origin': 'https://www.hotstar.com',
        'referer': 'https://www.hotstar.com/channels/starplus',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'x-client-code': 'LR',
        'x-country-code': 'IN',
        'x-platform-code': 'PCTV',
        'x-region-code': 'MH'
    }

# OPERATION
# get function to capture html from url
response = get(url)

# parse html into beautiful soup text object
#soup = BeautifulSoup(response.text, 'html.parser')
#type(soup)

# find_all function to extract html div containers w/ class attribute 'lister-item mode-advanced'
#containers = soup.find_all('body', 'article', class_ = 'ripple show-card normal') #need to check class_ call
#print(len(containers))

# acess title for all listings in containers
#name = containers.find_all('body', 'span', class_ = 'content-title ellipsise')

# access genre
#genre = containers.find_all('body', 'span', class_ = 'subtitle')

# access description
#description = containers.find_all('body', 'div', class_ = 'description ellipsize')

