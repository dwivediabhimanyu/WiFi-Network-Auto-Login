from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
f = open("cred.txt",'r',encoding = 'utf-8')
line=f.read()
f.close()
#Check if user is new or OLD
if(line=="#"):
    print("Hello New user! Please provide us your RPH Wifi username and password to auto login on your next start")
    print("Make sure you enter details correctly with Caps")
    usr=str(input("Username:"))
    psw=str(input("Password:"))
    flush=psw+"#"+usr
    f = open("cred.txt",'w',encoding = 'utf-8')
    f.write(flush)
    f.close()
    close=input("We have update our records. Please reopen the programme for updates to apply..\n Press any key to terminate")
    exit()
else:
    cred=line.split("#")
    print("Using saved details>>> Username: {} Password: {}".format(cred[1],cred[0]))
    passwordStr = cred[0]
    usernameStr = cred[1]
    browser = webdriver.Chrome()
    browser.get(('http://10.10.2.1/24online/webpages/client.jsp?fromlogout=true'))
    
    # fill in username and hit the next button
    
    username = browser.find_element_by_name('username')
    username.send_keys(usernameStr)
    
    password = browser.find_element_by_name('password')
    
    password.send_keys(passwordStr)
    
    signInButton = browser.find_element_by_name('login')
    signInButton.click()
