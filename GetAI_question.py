import re
import json
import requests
from bs4 import BeautifulSoup

url ='http://www.yaiedu.com/api/continue_answer'
data = {'answer_record_id':'678823'}
#Token和cookie需要更新
headers = {
            'Accept': 'application/vnd.edusoho.v2+json',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Conetent-Length':'23',
            'Conetent-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Proxy-Connection': 'keep-alive',
            'Host': 'www.yaiedu.com',
            'Origin': 'http://www.yaiedu.com',
            'Cookie':'online-uuid=4BD640D4-C217-9990-C38E-BF371B638D94; REMEMBERME=Qml6XFVzZXJcQ3VycmVudFVzZXI6ZFhObGNsOXBZemd4TnpKaVltMUFaV1IxYzI5b2J5NXVaWFE9OjE3MTIyMDEyNzM6ZmNjY2Q3MmVkN2UwNDdhMzdhNTNkYzZlOTY2NzY3NGUxZWY1YWFhMjRmMWUwMDJlZTY3MjY1MWZkN2VmYWFiZQ==; PHPSESSID=8jrrn58su68isbtn8r09r1or86',
            'Pragma':'no-cache',
            'Referer':'http://www.yaiedu.com/lesson/1193/testpaper/185/do',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            'X-CSRF-Token':'eegxDxe_p-QQYbxK3OjrizWT9H0jMINW84-kgAur-HE',
            'X-Requested-With':'XMLHttpRequest'
}
response = requests.post(data=data,url=url,headers=headers).json()
temp = json.dumps(response,indent=4,ensure_ascii=False)
# with open('test_data.json', 'w',encoding='utf-8') as json_file:
#     json_file.write(temp)
#items目录下进行变量遍历                      题型         题号
#题目

str_test = ''
for i in range(15):
    str_test = str_test + response['assessment']['sections'][0]['items'][i]['questions'][0]['stem']

#添加beautifulsoup 解析标签内容 拿到下载图片的链接
soup = BeautifulSoup(str_test,'html.parser') 
download_url = []
for i in soup.find_all('img'):
    download_url.append(i['src'])
for i in download_url:
    r = requests.get(url, allow_redirects=True)
    i.rsplit('/',1)[1]
print(download_url)

   
