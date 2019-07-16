from selenium import webdriver
from bs4 import BeautifulSoup
from wordcloud import WordCloud

f = open("homework1.txt",'w',encoding="UTF-8")
driver_path = '../resources/chromedriver' # driver path
url = 'https://post.naver.com/subject/list.nhn?navigationType=push&categoryNo=31&subjectType=CATEGORY&mainMenu=HEALTH' #건강/의학 포스트


browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
soup=browser.get(url)
page = browser.page_source

soup= BeautifulSoup(page, "html.parser")
links = soup.find_all('li') #각 포스트로 들어가기

for link in links: #텍스트 수집하기
    new_url = 'https://post.naver.com' + link.a['href']
    browser.get(new_url)
    page = browser.page_source
    soup = BeautifulSoup(page, "html.parser")
    new_links = soup.find_all('span', {'class': "se-ff-nanumgothic se-fs16 __se-node"})
    for text in new_links:
        print("text",text.getText())
        final_text = text.getText()
        f.write(final_text+"\n")
f.close()
browser.quit()

from konlpy.tag import Hannanum
from collections import Counter
import pytagcloud # Add fonts supporting Korean
f = open("homework1.txt", "r", encoding="UTF-8")
description = f.read()
# h = Hannanum()
# nouns = h.nouns(description)
# count = Counter(nouns)
# print(count)
# tag = count.most_common(100)
# tag_list = pytagcloud.make_tags(tag, maxsize=50)
# pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(900, 600), fontname='Korean',
# rectangular=False)

wordcloud = WordCloud(font_path='NanumBarunGothic.ttf',background_color='white',width=1200,height=800).generate(description)
wordcloud.to_file('wordcloud.png')

import webbrowser
webbrowser.open('wordcloud.png')