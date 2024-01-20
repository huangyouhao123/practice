url="https://m.bqg90.com/book/1637"

chapter=[i for i in range(1,100)]
import requests
from bs4 import BeautifulSoup

headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.0.10191 SLBChan/105',
}


def toText(url):
    response = requests.get(url, headers=headers)
    print(response)

    with open("novel.txt",'a') as fout:
        if response.status_code!=200:
            print("Error")
            return False

        else:
            soup=BeautifulSoup(response.text,"html.parser")
            strs=soup.find("div",id="chaptercontent").text

            fout.write(strs+"\n")
            print("success")

for i in chapter:
    Url=url+"/"+str(i)+".html"
    toText(Url)
    for page in range(2,10):
        Url=url+"/"+str(i)+"_"+str(page)+".html"
        if not toText(Url):
            break
        else:
            print("chapter:",i,"\t"+"page:",page)

