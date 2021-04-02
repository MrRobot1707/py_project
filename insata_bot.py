from selenium import webdriver

class Instabot():
	def __init__(self):
		#self.driver = webdriver.Edge(r"C:\Users\DELL\Desktop\python_project\msedgedriver.exe")chromedriver
		self.driver = webdriver.Chrome(r"C:\Users\DELL\Desktop\python_project\chromedriver.exe")
		self.driver.get("https://instagram.com")

Instabot()

