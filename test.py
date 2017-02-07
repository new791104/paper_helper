#測試用程式碼
import http.client
"""
result_id = 'result_box'
conn = http.client.HTTPSConnection("translate.google.com")
conn.request("GET", "/?source=gtx#en/zh-TW/test")
response = conn.getresponse()
data = response.read()

print(data.find(result_id))
"""
#print(response.status, response.reason)
#strstr(sStr1,sStr)

####request method####
import requests

from selenium import webdriver
"""
res = requests.get('https://translate.google.com/?source=gtx#en/zh-TW/test')
print(res.text)

soup = BeautifulSoup(res.text,"lxml")
for drink in soup.select('{}'.format("#result_box")):
    print(drink.get_text())"""
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\bin\phantomjs')  # PhantomJs
driver.get('https://translate.google.com/?source=gtx#en/zh-TW/test')  # 輸入範例網址，交給瀏覽器
res = driver.page_source  # 取得網頁原始碼
soup = BeautifulSoup(res,"lxml")
for drink in soup.select('{}'.format("#result_box")):
    print(drink.get_text())

driver.close()  # 關閉瀏覽器