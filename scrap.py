from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import csv 
import winsound
import pyttsx3



options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Arvi\AppData\Local\Google\Chrome\User Data") #Path to your chrome profile

driver = webdriver.Chrome(r'C:\Users\Arvi\Desktop\scrap-infinite-scroll\chromedriver.exe', chrome_options=options)
driver.get("https://www.bonumunion.com/parity/paritycat?type=0")

time.sleep(5)
data = []
print("scrolling")
i=0
while i<250:
    time.sleep(2)
    print(i,"calling")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    i+=1
time.sleep(5)
k = 0
soup=BeautifulSoup(driver.page_source,"html.parser")
divs = soup.find_all("div", class_="content van-row van-row--flex van-row--justify-center")
for div in divs:
    val = []
    pal = []
    div = soup.find_all('div','van-col van-col--5')
    period = soup.find_all('div','header__noe van-col van-col--9')
    for i in div:
        if(i.text!='Price' and i.text!='Number'):
            if(int(i.text)>10):
                val.append(int(i.text))
        #print("hai print",i.text)
    for j in period:
        if(j.text!=' Period'):
            pal.append(int(j.text))    
       
    if(k==0):
        #print("tatata!")
        break 
large_list = []
for i,j in zip(pal,val):
         large_list.append([i,j,j%10])

#print(large_list)





filename = "bonum.csv"
    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(["Period",'Price','Num'])  
        
    # writing the data rows  
    csvwriter.writerows(large_list) 
print(len(large_list))
freq = 500 
  
            
dur = 200

winsound.Beep(freq, dur) 
engine = pyttsx3.init() 
  

engine.say('Scraping is done') 
  
  
engine.runAndWait() 
               
winsound.Beep(freq, dur) 

print("::::::done::::::")