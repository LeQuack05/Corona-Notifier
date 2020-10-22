import bs4
import requests
from datetime import date
from push_notification import *

def scrapper(C,n):
    country=C
    html=f"https://www.worldometers.info/coronavirus/country/{country}"
    res=requests.get(html)
    soup=bs4.BeautifulSoup(res.text,"lxml")

    if n==1:
        cons=[]
        dict1={}
        for item in soup.select(".container #maincounter-wrap"):
            if item.text.strip()=='Projections':
                continue
            cons.append(item.text)
        
        upcons=[] 
        for item in cons:
            val=item.strip().replace("\n","")
            ls=val.split(':')
            upcons.extend(ls)
        
        d1={upcons[i]:upcons[i+1] for i in range(0,len(upcons),2)}
        total_cases(d1,country)
    
    if n==2:
        l1=[]
        for item in soup.select(f".col-md-12 #newsdate{date.today()} .news_post .news_ul strong"):
            l1.append(item.text)

        if l1==[]:
            empty_notification(country)
            return
        
        l2=[]

        for item in l1:
            st=item.split(' ')
            for i in st:
                if i=='new':
                    pass
                else:
                    l2.append(i)
               
        print(l2)
        if len(l2)>3:
            new_push(l2,1,country)
        else:
            new_push(l2,0,country)    
        
        