import requests

headers = {
    'authority': 'tianqi.2345.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '__bid_n=187c72bbc2862c259f4207; FPTOKEN=SR9A5k+Z3PiG8e5F72nsW3M37eZiZ+Di7Cre5ehNj5kkrqx9s/mNV/BOLNVHRyX+U5GH6kRzPtHlY7ErAD5F+o5uZgrj6Lx/CizIbot+3yLNoPH/o8FiobxSnI26h9bGtL0nR8BaasjeVgBxkM7STSQuhQ1xeCT8kmG8+p9WWWPjVtiZ4Rq4V+oy3ZwmOobXFWV02MRUV9WiokbMRFKfVfu1RLmfBT2TbVLSs4iYSo6JBmGuMvgbjXjN8ZBfZ93qwk98GHHg9cYT2ixG+TCPUoGKMhax4TPI12cTXswJVNvje4C1DHORVVLijEDmtdAWviGkddOAVrKPpqbf6gEaiIhKmO/Fs56E0nPJvD3j4syjtwahBmbt/Koz8iy7TO/+5rbBXHZOJjv62LDzmFdwsA==|5muMtyWjKzhWK/1K+MRXB4OR0wrZ8HEHxU83xH26/1s=|10|fefa8e81cc0a4da00fc94d126f5ff5c1; Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1704010384; positionCityID=71693; positionCityPinyin=huancui; lastCountyId=71693; lastCountyPinyin=huancui; lastProvinceId=31; lastCityId=54774; lastAreaName=?????\xa0; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1704011243; lastCountyTime=1704011243',
    'pragma': 'no-cache',
    'referer': 'https://tianqi.2345.com/wea_history/71693.htm',
    'sec-ch-ua': '"Chromium";v="9", "Not?A_Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.0.10191 SLBChan/105',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'areaInfo[areaId]': '71693',
    'areaInfo[areaType]': '2',
    'date[year]': '2018',
    'date[month]': '1',
}




import pandas as pd
df=pd.DataFrame()
for year in range(2018,2024):
    for month in range(1,13):
        params["date[year]"]=str(year)
        params["date[month]"]=str(month)
        response = requests.get('https://tianqi.2345.com/Pc/GetHistory', params=params, headers=headers)
        print(str(year)+" "+str(month))
        # print(response.text)
        print(response.text)
        data = response.json()["data"]
        table = pd.read_html(data)
        table=pd.DataFrame(table[0])
        df=pd.concat([df,table])


#print(df)
#df.to_excel("weather.xlsx")

