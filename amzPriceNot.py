import smtplib
import time
import requests
from bs4 import BeautifulSoup
from decimal import Decimal 
from re import sub
import time
url='https://www.amazon.in/Dell-Inspiron-3505-Integrated-D560483WIN9BE/dp/B097SZJ5Y4/ref=sr_1_2?crid=HSLCRBERN1XZ&dchild=1&keywords=dell+laptop&qid=1627727698&s=electronics&sprefix=dell+%2Celectronics%2C276&sr=1-2'

Header = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"}

emailAdd ='Email Add'
password= 'password'
myprice = 30000

def priceTrack():
	price = getPrice()
	if price > myprice:
		diff = price - myprice
		print(f"price more than Rs{diff} of your price")
	else:
		print("time to Buy..")
		sendEmail()

def sendEmail():
	subject='amazon price msg from python'
	# mailtext ="subject"+subject+"\n\n"+url
	body = url
	mailtext = f'Subject:{subject}\n\n{body}'
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(emailAdd,password)
	server.sendmail(emailAdd,"reviverEmail", mailtext)
	server.quit()
	print("email send")



def getPrice():
	page = requests.get(url,headers=Header)
	soup = BeautifulSoup(page.content,'html.parser')
	title = soup.find(id='productTitle').get_text().strip()
	price = soup.find(id='priceblock_ourprice').get_text().strip()[1:]
	value = int(Decimal(sub(r'[^\d.]', '', price)))
	print(value)
	return value
if __name__=='__main__':
	# while True:
	# 	priceTrack()
	# 	time.sleep(1)
	priceTrack()
