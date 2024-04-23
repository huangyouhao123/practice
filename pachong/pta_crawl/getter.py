import requests
import pandas as pd
from bs4 import BeautifulSoup
import requests

cookies = {
    '_bl_uid': 'd1l2nmds7IwfdXgm28F9tqCg48Re',
    '__snaker__id': 'CojY2yISF1Jav8zz',
    '_ga': 'GA1.1.189212980.1667219689',
    'PTASession': '0efe28ca-06e6-4c22-aeb7-9c6b3d235605',
    '_ga_ZHCNP8KECW': 'GS1.1.1705671115.9.1.1705671187.49.0.0',
    'JSESSIONID': '4C9BFAE3188D7441F93919D362BC1A71',
}

headers = {
    'authority': 'pintia.cn',
    'accept': 'application/json;charset=UTF-8',
    'accept-language': 'zh-CN',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': '_bl_uid=d1l2nmds7IwfdXgm28F9tqCg48Re; __snaker__id=CojY2yISF1Jav8zz; _ga=GA1.1.189212980.1667219689; PTASession=0efe28ca-06e6-4c22-aeb7-9c6b3d235605; _ga_ZHCNP8KECW=GS1.1.1705671115.9.1.1705671187.49.0.0; JSESSIONID=4C9BFAE3188D7441F93919D362BC1A71',
    'eagleeye-pappname': 'eksabfi2cn@94d5b8dc408ab8d',
    'eagleeye-sessionid': 'p7lmqr3nkFpovelL9362cg6caL9C',
    'eagleeye-traceid': 'e417852c170567119790510058ab8d',
    'pragma': 'no-cache',
    'referer': 'https://pintia.cn/problem-sets/1725039581707796480/exam/rankings',
    'sec-ch-ua': '"Chromium";v="9", "Not?A_Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.0.10191 SLBChan/105',
    'x-lollipop': '6af3a996b56d3ca2a850e76f26965e85',
    'x-marshmallow': '',
}


df=pd.DataFrame()

for page in range(3):
    params = {
        'page': str(page),
        'limit': '50',
    }

    response = requests.get(
        'https://pintia.cn/api/problem-sets/1725039581707796480/rankings',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    table=pd.DataFrame(response.json()['commonRankings']['commonRankings'])
    print(table)
    df = pd.concat([df, table])
print(df)
df.to_excel("pta2.xlsx")
