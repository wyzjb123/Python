import re
import json
import requests

url ='http://www.yaiedu.com/api/continue_answer'
data = {'answer_record_id':'678823'}
headers = {
            'Accept': 'application/vnd.edusoho.v2+json',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Conetent-Length':'23',
            'Conetent-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Proxy-Connection': 'keep-alive',
            'Host': 'www.yaiedu.com',
            'Origin': 'http://www.yaiedu.com',
            'Cookie':'online-uuid=4BD640D4-C217-9990-C38E-BF371B638D94; PHPSESSID=frnjc92jhal89qeucbep30v5m7; REMEMBERME=Qml6XFVzZXJcQ3VycmVudFVzZXI6ZFhObGNsOXBZemd4TnpKaVltMUFaV1IxYzI5b2J5NXVaWFE9OjE3MTIyMDEyNzM6ZmNjY2Q3MmVkN2UwNDdhMzdhNTNkYzZlOTY2NzY3NGUxZWY1YWFhMjRmMWUwMDJlZTY3MjY1MWZkN2VmYWFiZQ==',
            'Pragma':'no-cache',
            'Referer':'http://www.yaiedu.com/lesson/1193/testpaper/185/do',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            'X-CSRF-Token':'MZgBUYtyJoxSYSZpkZ-WXvVyQvcat0uu2HMenqq8ars',
            'X-Requested-With':'XMLHttpRequest'
}
response = requests.post(data=data,url=url,headers=headers).json()
temp = json.dumps(response,indent=4,ensure_ascii=False)
# with open('test_data.json', 'w',encoding='utf-8') as json_file:
#     json_file.write(temp)
#items目录下进行变量遍历                  题型         题号
#题目
question = response['assessment']['sections'][0]['items'][0]['questions'][0]['stem'])
