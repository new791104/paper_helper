from bs4 import BeautifulSoup
from selenium import webdriver
filename = "a.txt"

readfile = open(filename,'r')
writefile = open("output.txt","w")
paragraph_eng = ""
paragraph_ch = ""

with open(filename) as file:
    lines = (line.strip('\r\n') for line in file)  #lines 是底下 for迴圈 的 generator, string.strip() 是一個刪減字串的方法
    for line in lines:
        paragraph_eng += line
        #print(line,end='')

driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\bin\phantomjs')  #開啟PhantomJs瀏覽器
driver.get('https://translate.google.com/?source=gtx#en/zh-TW/' + paragraph_eng)  # 輸入範例網址，交給瀏覽器
res = driver.page_source  # 取得網頁原始碼
soup = BeautifulSoup(res,"lxml")
for drink in soup.select('{}'.format("#result_box")):
    #print(drink.get_text())
    paragraph_ch += drink.get_text()

writefile.write(paragraph_ch)
driver.close()  # 關閉瀏覽器
readfile.close()
writefile.close()

