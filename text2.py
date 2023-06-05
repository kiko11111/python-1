import requests 
from bs4 import BeautifulSoup
import lxml

import xlwt
import xlrd

wb = xlwt.Workbook()
ws = wb.add_sheet('test')

i=0
j=0

for x in range(1,2):
    # 牛客网竞赛排行榜链接
    url_1 = 'https://ac.nowcoder.com/acm/contest/rating-index?pageSize=50&searchUserName=&onlyMyFollow=false&page='+str(x)
    
    headers_1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    
    strhtml_1 = requests.get(url_1, headers=headers_1)  # Get方式获取网页数据
    
    soup_1 = BeautifulSoup(strhtml_1.text, 'lxml')
    
    post_list_1 = soup_1.find_all("td",class_="txt-left") #用户链接的div所在地址
    
    for post_1 in post_list_1:
        link_1 = post_1.find_all("a")[0]   #获取用户链接一部分

        print(link_1['href'])   # 输出用户名链接的一部分
        print(post_1)

        ws.write(i,j,link_1['href']) #保存链接


        url_2 = 'https://ac.nowcoder.com'+link_1['href']+'/practice-coding'  #连接链接成完整的部分
        headers_2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
        strhtml_2 = requests.get(url_2, headers=headers_2)  # Get方式获取网页数据
        soup_2 = BeautifulSoup(strhtml_2.text, 'lxml')  

        post_3 = soup_2.find_all("div","status-item")[0]  #用户竞赛分数所在div
        link_2 = post_3.find_all("a")[0]   #获取用户竞赛分数

        print(link_2.text.strip())
        print(link_2)

        j+=1
        ws.write(i,j,link_2.text.strip())

        
        post_list_2 = soup_2.find_all("div",class_="state-num")  #用户做题信息所在div
        for post_2 in post_list_2:  
            j+=1
            ws.write(i,j,post_2.text.strip())   #保存信息

            # print(post_2.text.strip())
            # print(post_2)

        j=0
        i+=1

# wb.save('test.xls')   #保存到excel表