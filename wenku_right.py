import requests
import re
import json

class WenKu():
    def __init__(self):
        self.session = requests.Session()

    def get_url(self):
        url = input("请输入下载的文库URL地址：")
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'wenku.baidu.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        }
        response = self.session.get(url=url,headers=headers)

        json_data = re.findall('"json":(.*?}])', response.text)[0]
        json_data = json.loads(json_data)
        # print(json_data)
        for index, page_load_urls in enumerate(json_data):
            # print(page_load_urls)
            page_load_url = page_load_urls['pageLoadUrl']
            # print(index)
            self.get_data(index, page_load_url)

    def get_data(self, index, url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'wkbjcloudbos.bdimg.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        }
        response = self.session.get(url=url,headers=headers)
        # print(response.content.decode('unicode_escape'))
        data = response.content.decode('unicode_escape')
        comand = 'wenku_' + str(index+1)
        json_data = re.findall(comand + "\((.*?}})\)", data)[0]
        # print(json_data)
        json_data = json.loads(json_data)
        result = []
        for i in json_data['body']:
            data = i["c"]
            # print(data)
            result.append(data)

        print(''.join(result).replace('    ', '\n'))
        print("")
        with open('百度文库2.docx', 'a', encoding='utf-8') as f:
            f.write('')
            f.write(''.join(result).replace('    ', '\n'))

if __name__ == '__main__':
    wk = WenKu()
    wk.get_url()