# -*- coding: gbk -*-
import csv

import requests
from lxml import etree
from urllib.parse import quote

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'cookie': '_T_WM=38421632912; XSRF-TOKEN=9d769d; SUB=_2A25IixCvDeRhGeNN6VoW-CjNwj2IHXVr6SxnrDV6PUJbktCOLXD9kW1NSdAvblt5gXfrGkD0JNWVphHoUcPk8JbM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhS18_-XbYHBibaJUr1c7sv5NHD95Qfe0zRS0nceK.pWs4Dqcjgi--ciKLFi-z4i--ciK.4iK.ceKzpeBtt; SSOLoginState=1703895296; MLOGIN=1; WEIBOCN_FROM=1110106030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%2523%25E6%2597%25A5%25E6%259C%25AC%25E6%25A0%25B8%25E6%25B1%25A1%25E6%25B0%25B4%26fid%3D100103type%253D1%2526q%253D%2523%25E6%2597%25A5%25E6%259C%25AC%25E6%25A0%25B8%25E6%25B1%25A1%25E6%25B0%25B4%26uicode%3D10000011; mweibo_short_token=4dd4e2e55e',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

page = 0
pageCount = 1
weibo_count = 0

baseUrl = 'https://s.weibo.com/weibo?q={}&Refer=index'
topic = '#日本核污水'
filename = topic.replace('#', '')

header = ['用户名称', '动态内容', '发表时间', '转发数量', '评论数量', '点赞数量']
f = open(f"{filename}.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.DictWriter(f, header, dialect="excel")
writer.writeheader()

url = baseUrl.format(quote(topic))

while True:
    page = page + 1
    tempUrl = url + '&page=' + str(page)
    print(tempUrl)
    response = requests.get(tempUrl, headers=headers)
    print(response.text.encode("utf-8"))
    html = etree.HTML(response.text, parser=etree.HTMLParser(encoding='utf-8'))
    articles = html.xpath('//div[@class="card-wrap"]')
    for article in articles[1:-4]:
        # 用户名
        user_name = article.xpath('div//div[@class="content"]/div/div/a/@nick-name')
        user_name = user_name[0] if user_name else '无用户名'
        # 动态内容
        article_content = article.xpath('div/div/div/p[@class="txt"]/text()')
        article_content = "".join(article_content).replace(" ", "").replace("\n", "").strip()
        # 发表时间
        publication_time = article.xpath('div//div[@class="from"]/a/text()')[0].strip()
        # 转发
        forward_count = article.xpath('div//div[@class="card-act"]/ul/li/a/text()')[1].strip()
        if forward_count == "转发":
            forward_count = 0
        # 评论
        comment_count = article.xpath('div//div[@class="card-act"]/ul/li/a/text()')[2].strip()
        if comment_count == "评论":
            comment_count = 0
        # 点赞
        like_count = article.xpath('div//span[@class="woo-like-count"]/text()')[-1].strip()
        if like_count == "赞":
            like_count = 0

        data_dict = {
            "用户名称": user_name,
            "动态内容": article_content,
            "发表时间": publication_time,
            "转发数量": forward_count,
            "评论数量": comment_count,
            "点赞数量": like_count
        }
        writer.writerow(data_dict)

        weibo_count = weibo_count + 1

        if user_name != "无用户名":
            print(f"当前微博数量：{weibo_count}\n".encode("gbk"),
                  f"用户名称：{data_dict['用户名称']}\n".encode("gbk"),
                  f"动态内容：{data_dict['动态内容']}\n".encode(""),
                  f"发表时间：{data_dict['发表时间']}\n".encode("gbk"),
                  f"转发数量：{data_dict['转发数量']}\n".encode("gbk"),
                  f"评论数量：{data_dict['评论数量']}\n".encode("gbk"),
                  f"点赞数量：{data_dict['点赞数量']}\n".encode("utf-8")
                  )

    try:
        if pageCount == 1:
            pageA = html.xpath('//*[@id="pl_feedlist_index"]/div[5]/div/a')[0].text
            pageCount = pageCount + 1
        elif pageCount == 100:
            print("没有下一页了")
            break
        else:
            pageA = html.xpath('//*[@id="pl_feedlist_index"]/div[5]/div/a[2]')[0].text
            pageCount = pageCount + 1
    except:
        print('没有下一页了')
        break

print('数据爬取完毕')

f.close()
