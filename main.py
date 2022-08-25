
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from progress.bar import *
from progress.spinner import MoonSpinner
import pandas as pd

START_URL ="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome('D:\programing\python\class\web scrapper\chromedriver.exe')
browser.get(START_URL)


with ChargingBar('loading',max=1000) as bar:
    for i in range(1000):
        time.sleep(0.01)
        bar.next()

with MoonSpinner('safety loading',max=20) as bar:
    for i in range(20):
        time.sleep(0.1)
        bar.next()


safe = lambda x :str(x).encode('utf-8')

#reion [rgba(0,0,0,1)] 
def scrape():
    headers = ["V Mag","Proper name","Bayer designation","Distance","Spectral class","Mass","Radius","Luminosity"]
    star_data = []
   
    soup=BeautifulSoup(browser.page_source, "html.parser")
    for tr in soup.find_all("tr"):
        td = tr.find_all("td")
        temp_list = []
        for index,a in enumerate(td):     
            match index: 
                case 0:
                    a.span.decompose()
                    if a.string is None:
                        a.span.decompose()
                        temp_list.append(str(a.string).replace(u'\u2212','-'))
                    else:
                        temp_list.append(str(a.string))
                case 1:
                    if a.find("a") is None:
                        temp_list.append(safe(a.string))
                    else:
                        temp_list.append(safe(a.find('a').string))
                case 2:
                    if a.string is None:
                        temp_list.append(safe(a.find('a').string))
                    else:
                        temp_list.append(safe(a.string))
                case 3:
                    if a.string is None:
                        a.span.decompose()
                        temp_list.append(str(a.string))
                    else:
                        temp_list.append(str(a.string))
                case 4:
                    temp_list.append(str(a.string))
                case 5:
                    temp_list.append(str(a.string))
                case 6:
                    temp_list.append(str(a.string))
                case 7:
                    temp_list.append(str(a.string))
            
          
            #print(temp_list)
            star_data.append(temp_list)
            
    with open("final.csv","w") as f:
        a=csv.writer(f)
        a.writerow(headers)
        a.writerows(star_data)
    
    
        
#endregion        
       
        
        



scrape()


