import requests
from bs4 import BeautifulSoup
import os
import time

sessions = requests.session()
list1 = []

# 爬取网站
url = 'http://www.dashenxiaoshuo.com/html/33/33228/'

def crawling():
    # 检测当前目录下存不存在小说的文件夹若不存在则创建
    if not os.path.exists('novel'):
        os.mkdir('novel')
    r = sessions.get(url)
    r.encoding='gbk'
    soup = BeautifulSoup(r.text, 'lxml')
    
 
    # 获取每章节链接
    dd = soup.find_all('dd')
    for i in range(len(dd)):
        ans = dd[i].a.get('href')
        link = ans.split('/',4)
        
        # 获取文本内容
        article_url = url + link[4]
        article_visit = sessions.get(article_url)
        article_visit.encoding='gbk'
        visit_result = BeautifulSoup(article_visit.text, 'lxml')

        # 写入小说内容
        for x in visit_result.find_all(id='content'):
            with open('novel/' + dd[i].a.get_text() + '.txt','w',encoding='utf-8') as f:
                f.write(x.get_text())
            
        
if __name__ == '__main__':
    crawling()
