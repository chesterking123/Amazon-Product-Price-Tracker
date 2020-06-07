import requests
from bs4 import BeautifulSoup
import re
import smtplib 
import time

URL = input("Enter URL of the item : ")
''''https://www.amazon.in/Acer-AN715-51-Notebook-i5-9300H-processor/dp/B0815BJ2Y4/ref=sr_1_3?dchild=1&keywords=1660ti+laptop&qid=1591510215&sr=8-3'''

current_price = float(input('Enter its current price : '))
'''76990'''

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

def find_price():
    
    page = requests.get(URL,headers=headers)
    
    soup = BeautifulSoup(page.content,'html.parser')
    
    title = soup.find(id = 'productTitle').get_text()
    
    price = soup.find(id = 'priceblock_ourprice').get_text()
    price = price[1:8]
    number_price = re.sub("\D","",price)
    
    print('\n Your item : ',title.strip())
    print('\nCurrent price : ',current_price)
    print('\n You will recieve an email when its price will drop \n Please check your spam section too :)')
    
    if(float(number_price) < current_price):
        send_email()
    

def send_email():
   
    email = ["deep.contractor88@gmail.com"] 
      
    for emails in email: 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("amazonpricedropbot@gmail.com", "Amazon@123") 
        subject = 'Price Drop Alert'
        body =  "There is a price drop in your Amazon Item !!! Check it out https://www.amazon.in/Acer-AN715-51-Notebook-i5-9300H-processor/dp/B0815BJ2Y4/ref=sr_1_3?dchild=1&keywords=1660ti+laptop&qid=1591510215&sr=8-3"
        message = f"Subject:{subject}\n\n{body}"
        s.sendmail("amazonpricedropbot@gmail.com", emails, message) 
        print('Alert! Email Sent')
        s.quit()    

while(True):
    find_price()
    time.sleep(18000)
