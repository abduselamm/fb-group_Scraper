from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
users={'profile':[],'profile_link':[]}
df = pd.read_csv('fb_users.csv')
chrome_driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get('https://www.facebook.com/groups/DubaiSchoolGuide/members')
#driver.maximize_window()
time.sleep(3)
loginId ='abduselamm555@gmail.com'
my_password='al0925962096'
user_name = driver.find_element(By.XPATH,'//*[@id="email"]')
user_name.send_keys("abduselamm555@gmail.com")

password = driver.find_element(By.XPATH,'//*[@id="pass"]')
password.send_keys(my_password)
log_in_button = driver.find_element(By.XPATH,'//*[@id="loginbutton"]')
log_in_button.click()
one='x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x9f619 x78zum5 x1r8uery x1iyjqo2 xs83m0k x1qughib x11i5rnm x1mh8g0r x2lwn1j xeuugli x4uap5 xkhd6sd x1n2onr6 x1ja2u2z x1qjc9v5 xdt5ytf xat24cr xdj266r xz9dl7a xsag5q8'
two='x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x9f619 x78zum5 x1r8uery x1iyjqo2 xs83m0k x1qughib x11i5rnm x1mh8g0r x2lwn1j xeuugli x4uap5 xkhd6sd x1n2onr6 x1ja2u2z x1qjc9v5 xdt5ytf xat24cr xdj266r xz9dl7a xsag5q8'
time.sleep(30)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

# member = driver.find_element(By.XPATH, '//*[@id="mount_0_0_bM"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[1]/h2/span/span')
# print(member.text)
# n=input("enter\n")

# nn=driver.find_element(By.XPATH,'//*[@id="mount_0_0_Oo"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a')
# print(nn.text)

print('hhhhhhhhhhh')