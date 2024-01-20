URL="https://pic.netbian.com/4kdongman/"
import requests
from bs4 import BeautifulSoup
import os

pages=[i for i in range(1,11)]
for page in pages:
    url=URL+"index_"+str(page)+".html"
    response=requests.get(url)
    response.encoding="gbk"
    print(response.status_code)
    html=response.text
    soup=BeautifulSoup(html,"html.parser")
    imgs=soup.find_all("img")
    for img in imgs:
        src=img["src"]
        if "/uploads" not in src:
            continue
        src=f"https://pic.netbian.com{src}"
        print(src)
        file_name=os.path.basename(src)
        with open(f"F:photos/{file_name}","wb") as fout:
            response_img=requests.get(src)
            fout.write(response_img.content)
