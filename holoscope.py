import requests
from bs4 import BeautifulSoup
import datetime

class holoscope:
    urlFormat = "https://fortune.yahoo.co.jp/12astro/{}/{}.html"
    zodiacSines = ["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
    zodiacSinesJa=["おひつじ座","おうし座","ふたご座","かに座","しし座","おとめ座","てんびん座","さそり座","いて座","やぎ座","みずがめ座","うお座"]
    def __init__(self,date,zodiacSineNum):
        self.date=date
        self.zodiacSineNum=zodiacSineNum
        self.zodiacSine=self.zodiacSines[zodiacSineNum]
        self.zodiacSineJa=self.zodiacSinesJa[zodiacSineNum]
    def __lt__(self,other):
        return self.point > other.point
    def getpoint(self):
        r = requests.get(self.urlFormat.format(self.date,self.zodiacSine))
        #print(self.urlFormat.format(self.date,self.zodiacSine))
        soup = BeautifulSoup(r.text, 'html.parser')
        elemspoint = soup.find("div", class_="bg01-03")
        self.point = int(elemspoint.find("p").getText()[:2])
        elemscomment = soup.find("div", class_="yftn12a-md48")
        self.comment=elemscomment.find("dt").getText()
now=datetime.date.today()
print(now,"いつの占いを出しますか？今日なら０を入力")
ddate=1
now=now+datetime.timedelta(days=ddate)
date="{}{:0>2}{:0>2}".format(now.year,now.month,now.day)
holoscopes=[]
for i in range(12):
    x=holoscope(date,i)
    x.getpoint()
    holoscopes.append(x)
holoscopes.sort()
circleNum=["①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩","⑪","⑫"]
output1="{month}月{day}日の十二星座占い　ℬ𝓎 𝓇𝓊𝒾𝒶".format(month=now.month,day=now.day)
output2="順位　星座　　　　点数"
outputForm="{}位　{:　<5}　{: <3}点"
print(output1)
print(output2)
for i in range(12):
    print(outputForm.format(circleNum[i],holoscopes[i].zodiacSineJa,holoscopes[i].point))
    print("　　"+holoscopes[i].comment)
