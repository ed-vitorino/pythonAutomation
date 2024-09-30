from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

website = "https://averdade.org.br/"
path = "/usr/bin/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
time.sleep(2)

containers = driver.find_elements(by="xpath", value='//div[@class="td-module-meta-info"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./h3').text
    link = container.find_element(by="xpath", value='./h3/a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitles)
    links.append(links)


my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')

driver.quit()