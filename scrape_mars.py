from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import os
import time
import requests
import warnings
warnings.filterwarnings('ignore')

def init_browser():
    # @NOTE: Path to my chromedriver
    executable_path = {"executable_path": "C:\\Users\\andre\\Desktop\chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

    mars_info = {}

    def scrape_mars_news():
        browser = init_browser()
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')

        news_title = soup.find('div', class_ = 'content_title').find('a').text
        news_p = soup.find('div', class_= 'article_teaser_body').text

        mars_info['news_title']= news_title
        mars_info['news_paragraph']= news_p

        return mars_info

        browser.quit()

def scrape_mars_image():
    browser = init_browser()

    featured_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featured_img_url)
    html_image = browser.html
    soup = bs(html_image, 'html.parser')

    image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    main_url = 'https://www.jpl.nasa.gov'
    img_url = main_url + image_url
    img_url
    mars_info['img_url'] = img_url

    return mars_info
    browser.quit

def scrape_mars_facts():
    browser = init_browser()

    url = 'http://space-facts.com/mars/'
    browser.visit(url)

    tables = pd.read_html(url)
    df = tables[1]

    df.columns = ['Description', 'Value']
    html_table = df.to_html(table_id="html_tbl_css", justify="left", index=False)

    mars_info['tables'] = html_table
    return mars_info


def scrape_mars_hemispheres():
    browser = init_browser()

    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)

    html_hemispheres = browser.html
    soup = bs(html_hemispheres, 'html.parser')
    items = soup.find_all('div', class_='item')
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    for i in items: 
            title = i.find('h3').text
            
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
             
            browser.visit(hemispheres_main_url + partial_img_url)
             
            partial_img_html = browser.html
             
            soup = bs( partial_img_html, 'html.parser')
             
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
             
            hiu.append({"title" : title, "img_url" : img_url})

    mars_info['hiu'] = hiu
        
       
    browser.quit()

  

    return mars_info