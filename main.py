# coding = MS950
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

filename = "a.txt"

block_size = 5
readfile = open(filename, 'r', encoding='utf-8-sig')
writefile = open("output.txt", 'w', encoding='utf-8-sig')
paragraph_eng_list = ['']
paragraph_ch_list = ['']
driver = webdriver.PhantomJS(executable_path=os.path.abspath(r'./phantomjs-2.1.1-windows/bin/phantomjs'))  # 開啟 PhantomJs 瀏覽器
driver.set_page_load_timeout(30)

### translate2ch ###
def translate2ch(paragraph_eng):  # 將段落翻譯成中文
    print("input: " + paragraph_eng)
    paragraph_ch = ""
    driver.get('https://translate.google.com/?source=gtx#en/zh-TW/' + paragraph_eng)  # 輸入範例網址，交給瀏覽器
    time.sleep(3)
    res = driver.page_source  # 取得網頁原始碼
    soup = BeautifulSoup(res, "lxml")  # BeautifulSoup 會使用指定的解析器將讀到的 html 解析成我們方便使用的形式，這裡使用 lxml 解析器
    for drink in soup.select('{}'.format("#result_box")):  # 找到 id 為 result_box 的欄位
        print(drink.get_text())
        if drink.get_text() == "":  # 若翻譯失敗，重送
            return translate2ch(paragraph_eng)
        else:
            paragraph_ch += drink.get_text()
    return paragraph_ch
### translate2ch end ###

#### main ####
with readfile as file:
    lines = (line.rstrip('\r\n') for line in file)  # lines 是底下 for迴圈 的 generator, string.strip() 是一個刪減字串的方法
    i = 0
    for line in lines:
        line = line.replace('/', '\\')
        line += " "  # 每一行補上一個空白
        paragraph_eng_list[i] += line
        if line == "" and paragraph_eng_list[i] != "":  # 分段，丟到 google翻譯
            paragraph_eng_list.append('')
            #translate2ch(paragraph_eng_list[i])
            writefile.write(translate2ch(paragraph_eng_list[i]))
            i += 1
    #translate2ch(paragraph_eng_list[i])
    writefile.write(translate2ch(paragraph_eng_list[i]))  # 最後一段的翻譯

driver.close()  # 關閉瀏覽器
readfile.close()
writefile.close()
#### main end ####





