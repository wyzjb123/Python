import re
import requests

url ='http://www.yaiedu.com/api/continue_answer'
headers = {
            'Accept': 'application/vnd.edusoho.v2+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Conetent-Length':'23',
            'Conetent-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Proxy-Connection': 'keep-alive',
            'Host': 'http://www.yaiedu.com',
            'Origin': 'http://www.yaiedu.com',
            'Cookie':'online-uuid=3852EE71-57EF-DD53-4FE0-36793C58D52A; PHPSESSID=a2afm17t3pf2cq555r3iger4c0; REMEMBERME=Qml6XFVzZXJcQ3VycmVudFVzZXI6ZFhObGNsOXBZemd4TnpKaVltMUFaV1IxYzI5b2J5NXVaWFE9OjE3MDE5MTU3NTE6MWE1YmE2OWVkNjNkNDRmYmRjOTBmMmQzODMxNDg0YjNhN2FlN2QxOTIyMzcxOTdhOGM3ZDUxOGQ1MGYxYTY5YQ==',
            'Pragma':'no-cache',
            'Referer':'http://www.yaiedu.com/lesson/526/testpaper/51/do',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            'X-CSRF-Token':'7HP1ixRDuNYFW5p8R6Fy4N0eR4BIXhVLJTezxUqlX14',
            'X-Requested-With':'XMLHttpRequest'
}
r = requests.Session()
r = r.get(url=url,headers=headers,)

print(r.text)

