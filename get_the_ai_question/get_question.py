import json

f = open('get_the_ai_question\青少年人工智能技术水平测试（一级）模拟测试卷01.json')

data = json.load(f)
for i in data['stem']:
    print(i)