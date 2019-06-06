# encoding:utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def  href(url):
    i = 0
    hreflist = []
    #打开网站
    chrome = webdriver.Chrome()
    chrome.get(url)
    #解析网站
    while(i<1):
        soup = BeautifulSoup(chrome.page_source,'lxml')    #将网站用beautiful soup解析
        alist = soup.select('div.cell > a[class=""]')      #找每个网站的链接
        for href in alist:
            href = 'https://job.bytedance.com' + href.get('href')
            hreflist.append(href)
        i = i + 1
        chrome.find_element_by_class_name("btn-next").click()   #用element模拟点击下一页
        time.sleep(2)
    #关闭网站
    chrome.close()
    return hreflist


hreflist = href("https://job.bytedance.com/society?summary=874&city=11&q1=&position_type=")
i = 0
file = open('D:/test.txt', 'w')
for a in hreflist:
    chrome = webdriver.Chrome()
    chrome.get(a)
    soup = BeautifulSoup(chrome.page_source, 'lxml')
    job_title = soup.select('div.job-title > span')
    job_dec = soup.select('div.job-content > div:nth-of-type(1) > pre')
    job_req = soup.select('div.job-content > div:nth-of-type(2) > div > pre')

    for fp in job_title:
        file.write(str(fp))
        file.write('\n')

    for fp1 in job_dec:
        file.write(str(fp1))
        file.write('\n')

    for fp2 in job_req:
        file.write(str(fp2))
        file.write('\n')
        file.write('\n')

    time.sleep(1)
    i = i + 1
    print i
file.close()