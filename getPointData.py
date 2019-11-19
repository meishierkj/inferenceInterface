# -*- coding: utf-8 -*-
# @Time         : 2019/11/05
# @Author       : WKJ
# @Description  :
import urllib.request
import json
import time
from collections import OrderedDict

def getData(Authorization):

    #时序库查询特征数据
    url = 'http://10.6.9.39:15016/api/v1/data/namespace/thermalpower/timeseries/features/types/Inference_Engine_Feature/select'
    headers = {
        'Authorization': Authorization,
        'Content-Type': 'application/json'
    }

    #获取当前时间及前十秒时间，时间格式：2019-11-06 01:24:59 2019-11-06 01:24:49
    f = time.time()
    t = f - 10
    local_f = time.gmtime(f)
    local_t = time.gmtime(t)
    pub_f = time.strftime('%Y-%m-%d %H:%M:%S', local_f)
    pub_t = time.strftime('%Y-%m-%d %H:%M:%S', local_t)

    #Request Body
    values = {"thingId":"Inference_Engine", "fields": ["MAJ03001","MAJ03002","MAJ03003","MAJ03004","MAJ03005","MAJ03006","MAJ03007","MAJ03008","MAJ03009","MAJ03010","MAJ03011","MAJ03012","MAJ03013","MAJ03014","MAJ03015","MAJ03016"], "startTime": pub_f,"endTime": pub_t,"sort": "asc"}
    data = json.dumps(values)
    data = bytes(data, 'utf8')

    req = urllib.request.Request(url, headers=headers, data=data)
    response = urllib.request.urlopen(req)
    output = response.read().decode('utf-8')
    #print(output)

    if len(output):
        obj = json.loads(output,object_pairs_hook=OrderedDict)
        s = obj['data']
        n = obj['code']
        # 通过list将字典中的values转化为列表,取第一个数值
        # a = list(s.values())
        # b = len(a)
        # print(len(a))
        # print(a[b-1])
        #print(list(s.values())[0])
        if n == 200:
            data = []
            if len(s):
                # 获取最新数据
                for key, value in s.items():
                    dic = {}
                    dic['time'] = key
                    dic['value'] = list(value)
                    data.append(dic)
                return json.dumps({'code': 200, 'data': data[len(data)-1]})
            else:
                return json.dumps({'code:': 200,'data':'null'})
        else:
            return json.dumps({'code:': 500,'message':'data failed'})