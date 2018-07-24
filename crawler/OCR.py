import requests, json, base64

def OCR_captcha(filename):
    print('starting OCR...')
    with open(filename, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        OCR_url = 'http://op.juhe.cn/vercode/index'
        params = {
            "key": "fadea6d418df1ce13d42f380178bed71",  # 您申请到的APPKEY
            "codeType": "1004",
            'base64Str': base64_data,
            "dtype": ""  # 返回的数据的格式，json或xml，默认为json
        }
        OCR = requests.get(OCR_url, params=params)
        res = json.loads(OCR.content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                # 成功请求
                print('OCR result: ' + res["result"])
                return res['result']
            else:
                print("%s:%s" % (res["error_code"], res["reason"]))
                return ''
        else:
            print("request api error")
            return ''
