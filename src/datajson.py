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
    "����": "����",
    "�Ա�": true,
    "����": 25,
    "��������": "20110924",
    "��������": "20111020",
    "������Ŀ":
    [
        "ֱ̧��100��",
        "��̧��200��",
        "�ױ��˶�300��"
    ],
    "�ƻ�":
    [
        {
            "����": [2011,10,21],
            "��Ŀ":
                [
                    {"index": 1, "flag": true},
                    {"index": 1, "flag": true}
                ],
            "����": "",
            "��־": "����о�����"
        },
        {
            "����": [2011,10,21],
            "��Ŀ":
                [
                    {"index": 1, "flag": true},
                    {"index": 1, "flag": true}
                ],
            "����": "",
            "��־": "����о�����"
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
