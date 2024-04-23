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
topic = '#�ձ�����ˮ'
filename = topic.replace('#', '')

header = ['�û�����', '��̬����', '����ʱ��', 'ת������', '��������', '��������']
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
        # �û���
        user_name = article.xpath('div//div[@class="content"]/div/div/a/@nick-name')
        user_name = user_name[0] if user_name else '���û���'
        # ��̬����
        article_content = article.xpath('div/div/div/p[@class="txt"]/text()')
        article_content = "".join(article_content).replace(" ", "").replace("\n", "").strip()
        # ����ʱ��
        publication_time = article.xpath('div//div[@class="from"]/a/text()')[0].strip()
        # ת��
        forward_count = article.xpath('div//div[@class="card-act"]/ul/li/a/text()')[1].strip()
        if forward_count == "ת��":
            forward_count = 0
        # ����
        comment_count = article.xpath('div//div[@class="card-act"]/ul/li/a/text()')[2].strip()
        if comment_count == "����":
            comment_count = 0
        # ����
        like_count = article.xpath('div//span[@class="woo-like-count"]/text()')[-1].strip()
        if like_count == "��":
            like_count = 0

        data_dict = {
            "�û�����": user_name,
            "��̬����": article_content,
            "����ʱ��": publication_time,
            "ת������": forward_count,
            "��������": comment_count,
            "��������": like_count
        }
        writer.writerow(data_dict)

        weibo_count = weibo_count + 1

        if user_name != "���û���":
            print(f"��ǰ΢��������{weibo_count}\n".encode("gbk"),
                  f"�û����ƣ�{data_dict['�û�����']}\n".encode("gbk"),
                  f"��̬���ݣ�{data_dict['��̬����']}\n".encode(""),
                  f"����ʱ�䣺{data_dict['����ʱ��']}\n".encode("gbk"),
                  f"ת��������{data_dict['ת������']}\n".encode("gbk"),
                  f"����������{data_dict['��������']}\n".encode("gbk"),
                  f"����������{data_dict['��������']}\n".encode("utf-8")
                  )

    try:
        if pageCount == 1:
            pageA = html.xpath('//*[@id="pl_feedlist_index"]/div[5]/div/a')[0].text
            pageCount = pageCount + 1
        elif pageCount == 100:
            print("û����һҳ��")
            break
        else:
            pageA = html.xpath('//*[@id="pl_feedlist_index"]/div[5]/div/a[2]')[0].text
            pageCount = pageCount + 1
    except:
        print('û����һҳ��')
        break

print('������ȡ���')

f.close()
