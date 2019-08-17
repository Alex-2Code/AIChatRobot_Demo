# @Version : 1.0
# @Time    : 2019/8/7
# @Author  : Ran


import json
import urllib.request


api_url = "http://openapi.tuling123.com/openapi/api/v2"
print('移协小AI：你好，我是移协小AI，今天聊点什么呢？')  #问候语

a = 0

while 1:
    text_input = input('我：')
    
    req = {
        "perception":
        {
            "inputText":
            {
                "text": text_input
            },
        },

        "userInfo": 
        {
            "apiKey": "你创建的机器人的API",  #机器人可在图灵机器人官网创建
            "userId": "用户的ID"    #你在图灵机器人官网的账号ID
        }
    }

    req = json.dumps(req).encode('utf8')

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')

    response_dic = json.loads(response_str)


    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    
    print('移协小AI：'+ results_text)
    
    a +=1
    
    if a>66:    #限制最多聊天次数，可更改，但是无法突破图灵机器人官网的限制！（普通认证的用户为100次/天）
        print('好了，今天聊得够多了，等你学会了我的代码，说不定我能多陪你聊几个小时，继续学习哦～加油💪💪')
        break

