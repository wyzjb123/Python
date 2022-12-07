import re
import requests

url ='http://www.yaiedu.com/api/continue_answer'
data = {'answer_record_id':'569015'}
headers = {
            'Accept': 'application/vnd.edusoho.v2+json',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Conetent-Length':'23',
            'Conetent-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Proxy-Connection': 'keep-alive',
            'Host': 'www.yaiedu.com',
            'Origin': 'http://www.yaiedu.com',
            'Cookie':'online-uuid=7946ACD4-2B0C-E2C1-3713-B418A94951B0; is_skip_mobile_bind=0; PHPSESSID=smusch6ecoduve0uv17qn8a230; REMEMBERME=Qml6XFVzZXJcQ3VycmVudFVzZXI6ZFhObGNsOXBZemd4TnpKaVltMUFaV1IxYzI5b2J5NXVaWFE9OjE3MDE5NzIwMTQ6ZWU2NjllOWYyMDI3NjQ4NDI5ODMwOTc0YmI3ZjBjNDNiZThlNmU4YjE5MjBlODAxOWI1NDM1ODAyYTA5ZDhhZQ==',
            'Pragma':'no-cache',
            'Referer':'http://www.yaiedu.com/lesson/526/testpaper/51/do',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            'X-CSRF-Token':'5bHd-jUvt--PXbJiho7NcggrdUO-ha0VDTQGP7xZDJM',
            'X-Requested-With':'XMLHttpRequest'
}
r = requests.Session()
response = r.post(data=data,url=url,headers=headers,)

print(response.status_code)

