import httplib, urllib, json
import os

srcPath=r"egg.jpg"
path=os.path.abspath(srcPath)
img = open(os.path.expanduser(srcPath), 'rb')

subscription_key = 'c3e4ced66c2e4ad191c75fb1745c7987'
uri_base = 'api.cognitive.azure.cn'

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.urlencode({
    'visualFeatures': 'Categories,Description',
    'details': '',
    'language': 'en',
})

body = '{"url":path}'

try:
    conn = httplib.HTTPSConnection('api.cognitive.azure.cn')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, img, headers)
    response = conn.getresponse()
    data = response.read()
    data = eval(data)
    for key1, value1 in data.items():
        if key1 == "description":
            for key2, value2 in value1.items():
                if key2 == "tags":
                    print(value2[0])

    conn.close()

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


