# -*- coding: utf-8 -*-
# @Time         : 2019/11/07
# @Author       : WKJ
# @Description  :
from flask import request
import urllib.request
import json
from collections import OrderedDict

def getDate():

    # 获取推理机来取数据时带着的token
    Authorization = request.headers.get('Authorization')
    #print(Authorization)

    #获取POST请求中的Body
    body = request.json
    #print(body)

    # 获取Body中的时间，时间格式：2019-11-06 01:24:59 2019-11-06 01:24:49
    f = body["timeon"]
    t = body["timeout"]
    #print(f,t)

    #获取Bod中的点名
    p = body["point"]
    #print(p)

    url = 'http://10.6.9.39:15016/api/v1/data/namespace/thermalpower/timeseries/features/types/Inference_Engine_Feature/select'
    headers = {
        'Authorization': Authorization,
        'Content-Type': 'application/json'
    }
    # Request Body
    values = {"thingId": "Inference_Engine","fields":[p],"startTime": f, "endTime": t, "sort": "asc"}
    data = json.dumps(values)
    data = bytes(data, 'utf8')
    #print(data)

    req = urllib.request.Request(url, headers=headers, data=data)
    response = urllib.request.urlopen(req)
    output = response.read().decode('utf-8')
    #print(output)

    if len(output):
        obj = json.loads(output,object_pairs_hook=OrderedDict)
        n = obj['code']
        if n == 200:
            return (obj)
        else:
            return json.dumps({'code:': 500,'message':'data failed'})