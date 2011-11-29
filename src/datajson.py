#!/usr/bin/python3

# -*- coding: UTF-8 -*-

import json

jdata1 = json.loads("""[
                "foo",
                {
                    "bar":
                    [
                        "baz",
                        null,
                        1.0,
                        2
                    ]
                }
              ]""")

print(jdata1)

jdata2 = json.loads("""{
    "姓名": "星宇",
    "性别": true,
    "年龄": 25,
    "受伤日期": "20110924",
    "手术日期": "20111020",
    "锻炼项目":
    [
        "直抬腿100次",
        "侧抬腿200次",
        "踝崩运动300次"
    ],
    "计划":
    [
        {
            "日期": [2011,10,21],
            "项目":
                [
                    {"index": 1, "flag": true},
                    {"index": 1, "flag": true}
                ],
            "肿胀": "",
            "日志": "今天感觉不错"
        },
        {
            "日期": [2011,10,21],
            "项目":
                [
                    {"index": 1, "flag": true},
                    {"index": 1, "flag": true}
                ],
            "肿胀": "",
            "日志": "今天感觉不错"
        }
    ]
    }""")

try:
    print(jdata2["firstName"])
except:
    pass

json.read("{a:10}")

class JsonData(object):
    """data as json format
    
    """
    
    def __init__(self, filePath):
        """init JsonData bounding with a file
        
        Arguments:
        - `filePath`:
        """
        self._filePath = filePath



if __name__ == '__main__':
    print('for json')
