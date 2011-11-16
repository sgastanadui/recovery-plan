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
    "": "John",
    "lastName": "Smith",
    "male": true,
    "age": 25,
    "address":
    {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021"
        },
    "phoneNumber":
    [
        {
            "type": "home",
            "number": "212 555-1234"
            },
        {
            "type": "fax",
            "number": "646 555-4567"
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
