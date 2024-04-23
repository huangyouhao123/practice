# coding: utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd

page_indexs = range(0, 250, 25)
list(page_indexs)
cookies = {
    'll': '"118220"',
    'bid': 'LOHSMlNHKwo',
    '__yadk_uid': 'QKBKzxCVaIG9Z26ArKHxMrBgXYRXVe0T',
    '__gads': 'ID=9f877f67f13c9167-222608eb63d9003f:T=1674572649:RT=1674572649:S=ALNI_MYKJwCupZADKPHTy-fszB_LXjtnpw',
    '__gpi': 'UID=00000bac03c721f3:T=1674572649:RT=1674572649:S=ALNI_MaXqpfyuz2wuhgiO0cMbMC3XdOlow',
    '_vwo_uuid_v2': 'D67A05F02E2DB9A6BB5622239B406738D|bb4f38d9bd483e7ff8ba10b7920259c5',
    '_pk_id.100001.4cf6': 'e9cb1922667611e1.1674572649.',
    'Hm_lvt_16a14f3002af32bf3a75dfe352478639': '1702299152',
    '__utmz': '30149280.1703903618.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    'dbcl2': '"276796991:C8oRWvuAjAM"',
    'push_noty_num': '0',
    'push_doumail_num': '0',
    '__utmv': '30149280.27679',
    '__utmz': '223695111.1703903739.4.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    'ck': 'NFTR',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1703990981%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    '_pk_ses.100001.4cf6': '1',
    'ap_v': '0,6.0',
    '__utma': '30149280.80446311.1674572649.1703903618.1703990981.5',
    '__utmb': '30149280.0.10.1703990981',
    '__utmc': '30149280',
    '__utma': '223695111.2146049854.1674572649.1703903739.1703990981.5',
    '__utmb': '223695111.0.10.1703990981',
    '__utmc': '223695111',
    'frodotk_db': '"110353427f9e16123309f9c77eda4236"',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'll="118220"; bid=LOHSMlNHKwo; __yadk_uid=QKBKzxCVaIG9Z26ArKHxMrBgXYRXVe0T; __gads=ID=9f877f67f13c9167-222608eb63d9003f:T=1674572649:RT=1674572649:S=ALNI_MYKJwCupZADKPHTy-fszB_LXjtnpw; __gpi=UID=00000bac03c721f3:T=1674572649:RT=1674572649:S=ALNI_MaXqpfyuz2wuhgiO0cMbMC3XdOlow; _vwo_uuid_v2=D67A05F02E2DB9A6BB5622239B406738D|bb4f38d9bd483e7ff8ba10b7920259c5; _pk_id.100001.4cf6=e9cb1922667611e1.1674572649.; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1702299152; __utmz=30149280.1703903618.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="276796991:C8oRWvuAjAM"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.27679; __utmz=223695111.1703903739.4.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ck=NFTR; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1703990981%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.80446311.1674572649.1703903618.1703990981.5; __utmb=30149280.0.10.1703990981; __utmc=30149280; __utma=223695111.2146049854.1674572649.1703903739.1703990981.5; __utmb=223695111.0.10.1703990981; __utmc=223695111; frodotk_db="110353427f9e16123309f9c77eda4236"',
    'Pragma': 'no-cache',
    'Referer': 'https://movie.douban.com/top250',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.0.10191 SLBChan/105',
    'sec-ch-ua': '"Chromium";v="9", "Not?A_Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def downlaoad_all_htmls():
    htmls = []
    for idx in page_indexs:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        print("crawl html:", url)
        r = requests.get(url, cookies=cookies, headers=headers)
        if r.status_code != 200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls


htmls = downlaoad_all_htmls()


def parse_single_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    article_items = [itm for itm in
                     soup.find("div", class_="article").
                     find("ol", class_="grid_view")
                     .find_all("div", class_="item")
                     ]
    datas = []
    for article_item in article_items:
        rank = article_item.find("div", class_="pic").find("em").get_text()
        info = article_item.find("div", class_="info")
        title = info.find("div", class_="hd").find("span", class_="title").get_text()
        stars = (
            info.find("div", class_="bd")
            .find("div", class_="star")
            .find_all("span")
        )
        rating_star = stars[0]["class"][0]
        rating_num = stars[1].get_text()
        comments = stars[3].get_text()
        datas.append({
            "rank": rank,
            "title": title,
            "rating_star": rating_star.replace("rating", "").replace("-t", ""),
            "rating_num": rating_num,
            "comments": comments.replace("人评价", "")
        })
    return datas


import pprint

pprint.pprint(parse_single_html(htmls[0]))
all_datas = []
for html in htmls:
    all_datas.extend(parse_single_html(html))
print(all_datas)

df=pd.DataFrame(all_datas)
df.to_excel("豆瓣评分.xlsx")
