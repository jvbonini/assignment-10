#%% [markdown]
# ### Declare Dependencies 

#%%
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests

#%% [markdown]
# ### Declare in Memory

#%%
# Drivers`s Path
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

#%% [markdown]
# ### NASA Mars |  News

#%%
# Nasa news url through splinter module
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


#%%
# Declare HTML Object
html = browser.html
# Create a Beautiful Soup object
soup = BeautifulSoup(html, 'html.parser')
# Retrieve the latest element that contains news title and news_paragraph
news_title = soup.find('div', class_='content_title').find('a').text
news_p = soup.find('div', class_='article_teaser_body').text
# Print out title and news
print(news_title)
print(news_p)

#%% [markdown]
# ### Mars Space Images | Jet Propulsion Laboratory

#%%
# Go to Mars Space Images through splinter module
image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url_featured)


#%%
# Declare HTML Object
html_image = browser.html
# Create a Beautiful Soup object
soup = BeautifulSoup(html_image, 'html.parser')
# Retrieve background-image url from style tag 
featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
# Website Url 
main_url = 'https://www.jpl.nasa.gov'
# Concatenate url with scrapped route
featured_image_url = main_url + featured_image_url
# Display full link to featured image
featured_image_url 

#%% [markdown]
# ### Mars Weather | Twitter

#%%
# Go to Mars Weather Twitter through splinter module
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)


#%%
# HTML Object 
html_weather = browser.html
# Create a Beautiful Soup object
soup = BeautifulSoup(html_weather, 'html.parser')
# Find all elements that contain tweets
latest_tweets = soup.find_all('div', class_='js-tweet-text-container')
# Retrieve all elements that contain news title in the specified range
# Look for entries that display weather related words to exclude non weather related tweets 
for tweet in latest_tweets: 
  weather_tweet = tweet.find('p').text
  if 'Sol' and 'pressure' in weather_tweet:
      print(weather_tweet)
      break
  else: 
      pass

#%% [markdown]
# ### Mars |  Facts

#%%
# Go to Mars facts url 
facts_url = 'http://space-facts.com/mars/'
# Create a Beautiful Soup object
mars_facts = pd.read_html(facts_url)
# Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
mars_df = mars_facts[0]
# Assign the columns `['Description', 'Value']`
mars_df.columns = ['Description','Value']
# Set the index to the `Description` column without row indexing
mars_df.set_index('Description', inplace=True)
# Save html code to folder Assets
mars_df.to_html()
data = mars_df.to_dict(orient='records')  
# Print out in the window
mars_df

#%% [markdown]
# ### Mars | Hemispheres

#%%
# Go to  hemispheres website through splinter module 
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)


#%%
# HTML Object
html_hemispheres = browser.html
# Create a Beautiful Soup object
soup = BeautifulSoup(html_hemispheres, 'html.parser')
# Retreive all items that contain mars hemispheres information
items = soup.find_all('div', class_='item')
# Create empty list for hemisphere urls 
hemisphere_image_urls = []
# Store the main_ul 
hemispheres_main_url = 'https://astrogeology.usgs.gov'
# Loop through the items previously stored
for i in items: 
    # Store title
    title = i.find('h3').text
    # Store link that leads to full image website
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    # Go to  the link that contains the full image website 
    browser.visit(hemispheres_main_url + partial_img_url)
    # HTML Object of individual hemisphere information website 
    partial_img_html = browser.html
    # Create a Beautiful Soup object for every individual hemisphere information website 
    soup = BeautifulSoup( partial_img_html, 'html.parser')
    # Retrieve full image source 
    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    # Append the retreived information into a list of dictionaries 
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
# Display hemisphere_image_urls
hemisphere_image_urls


