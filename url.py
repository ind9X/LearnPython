import re
from urllib import request
import requests
"""
url = 'https://www.qiushibaike.com/imgrank/'
re_jpg = re.compile(r'<img src="(.*?\.jpg)"')
req = request.Request(url,headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
})
response = request.urlopen(req)
html = response.read().decode('utf-8')
img_list = re_jpg.findall(html)
#print(img_list)
n = 0
for i in img_list:
    print("正在下载：https:%s" % i)
    request.urlretrieve("https:" + i, "./img/%s.jpg" % n)
    n += 1
"""
HtmlUrl = 'https://www.ivsky.com/tupian/harrison_lake_v38011/'
def ImgDown(HtmlUrl):
    ReJpg = re.compile(r'<img src="(.*?\.jpg)')
    UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    HtmlRequest = request.Request(HtmlUrl,headers={
        'User-Agent':UserAgent
    })
    HtmlResponse = request.urlopen(HtmlRequest)
    HtmlText = HtmlResponse.read().decode('utf-8')
    # print(HtmlText)
    ImgList = ReJpg.findall(HtmlText)
    n = 1
    for i in ImgList:
        print("正在下载第",n,"个：https:%s" % i)
        request.urlretrieve("https:" + i, "%s.jpg" % n)
        n += 1
ImgDown(HtmlUrl)