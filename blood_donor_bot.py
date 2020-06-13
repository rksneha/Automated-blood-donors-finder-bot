from selenium import webdriver
from twilio.rest import Client
import time
import timeit
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests

#driver.find_element_by_name("q").send_keys("Automation Step by Step")
#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
res= requests.get("https://ipinfo.io/")
data=res.json()
print("Your location")
print(res.text)
City=data['city']
#region=list(data['region'])
City=City.encode('utf-8')
k=[]
#for x in region:
#    h=x.encode('utf-8')
 #   k.append(h)
for i in range(1,len(k)):
    k[i]=k[i].lower()
#region=str(''.join(k))
#region = ''.join(region.split())
print("SEARCHING BLOOD DONORS NEAR YOU")
driver = webdriver.Chrome("chromedriver.exe")
driver.set_page_load_timeout(50)
driver.get("http://bloodworld.in/")
search_field=Select(driver.find_element_by_id("state"))
for opt in search_field.options:
    search_field.select_by_visible_text("Tamil Nadu")
driver.implicitly_wait(30)
s=Select(driver.find_element_by_id("district"))
for opt in search_field.options:
    s.select_by_visible_text(str(City))
driver.implicitly_wait(30)
sn=Select(driver.find_element_by_id("bloodgroup"))
for opt in search_field.options:
    sn.select_by_value('13')
driver.find_element_by_name("Search").click()
a=[]
k=[]
l=[]
j=0
rows=len(driver.find_elements_by_xpath("/html/body/div/div[2]/form/div[2]/table[2]/tbody/tr"))
print("Available PEOPLE'S CONTACT NUMBERS:")
for i in range(5,rows+1):
    col=driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/table[2]/tbody/tr["+str(i)+"]/td["+str(7)+"]").text
    a.append(col)
for x in a:
    h=x.encode('utf-8')
    k.append(h)
k = list(filter(None,k))
kl=[]

kl= ["+91" + x for x in k]
kl.append('+918610394149') #Dummy numbers has been used to test the project working.
kl.append('+918870808886')
print(kl)
account_sid = 'ACd367cf24b52e404508fcf948777f5dad'
auth_token = '2a4b8d7ad4a67a5ca78a6bef3189dd48'
my_cell = '+918610394147'
my_t = '+19382229888'
client = Client(account_sid,auth_token)
my_msg='click https://iplogger.org/3oDQp'
mymsg='please contact us urgently. 8610394147. O+ blood needed'
for i in range(len(kl)-2,len(kl)):
    message= client.messages.create(to=kl[i],from_=my_t,body=my_msg)
print(my_msg + "               ----this message is sent to them----------")
driver.get("https://iplogger.org/logger/k9tdh5y3oDQp/")
driver.implicitly_wait(50)
user=[]
driver.find_element_by_xpath("/html/body/div[12]/div/div/p[2]/label/span").click()
driver.find_element_by_xpath("/html/body/div[12]/div/div/p[3]/button").click()
a=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div[4]/div[2]/div[1]/div[2]").text
user.append(a)
a=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div[4]/div[2]/div[3]/div[2]").text
user.append(a)
print("DETAILS OF THE USERS WHO CLICKED:")
for i in range(0,len(user)):
    print(user[i])
driver.get("https://ipinfo.io/")
driver.find_element_by_xpath("/html/body/header/div/div/nav/div/div[2]/div/a[1]").click()
driver.find_element_by_id("username").send_keys("suchithra.295@gmail.com")
driver.find_element_by_id("password_v").send_keys("sweety295")
driver.find_element_by_xpath("/html/body/div/section/div/div/div/form/div[2]/button").send_keys(Keys.ENTER)
driver.implicitly_wait(50)
loc = []
driver.find_element_by_id("account-search-input").send_keys(user[0])
print("user-1's location:")
sne=driver.find_element_by_xpath("/html/body/div/div/section/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/span[2]").text;
sne=sne.encode('utf-8')
print(sne)
loc.append(sne)
driver.find_element_by_id("dashboard-search-input").clear()
driver.find_element_by_id("dashboard-search-input").send_keys(user[1])
print("user-2's location:")
sne=driver.find_element_by_xpath("/html/body/div/div/section/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/span[2]").text;
sne=sne.encode('utf-8')
print(sne)
loc.append(sne)
print(type(loc[0]))
for i in range(0,len(loc)):
    if(loc[i]=='"'+City+'"'):
        w=kl[len(kl)-1-i]
        print(w)
        print(user[i])
        print("is in "+ City)
        message = client.messages.create(to=w, from_=my_t, body=mymsg)
        print(mymsg + "               ----this message is sent to them----------")
    else:
        w=kl[len(kl)-1-i]
        print(w)
        print(user[i])
        print("not in "+City)
print("TIME TAKEN FOR THIS CODE:")

time.sleep(4)
driver.quit()

