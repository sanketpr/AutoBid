import re
import pickle
import sys
import time
import csv
import urllib2
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from BeautifulSoup import BeautifulSoup

try:
	link = sys.argv[1]
except:
	sys.exit("specify a link")

driver = webdriver.Firefox()

print "https://freelancer.com"
driver.get("https://freelancer.com")

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)


def operation_main(proj_link):

	#Directon 
	driver.get(proj_link)	

	try:
		driver.find_element_by_class_name("bidButton").click()
	except:
		print "not able to bid on this porject"
		return

	proj_budget = driver.find_element_by_class_name("project-budget").text
	lower_budget=[]
	higher_budget=[]
	proj_budget.replace("-","")
	proj_budget.replace(" ","")
	#if(proj_budget[0]!="$"):
	#	sys.exit()
	#i=0
	#while proj_budget[i+1]!="$":
	#	i+=1
	#	lower_budget.append(proj_budget[i])
	
	i=0
	#while proj_budget[len(proj_budget)-i-1]!="$" or proj_budget[len(proj_budget)-i-1]!=chr(128):
	#	i+=1
	#	higher_budget.append(proj_budget[len(proj_budget)-i])
	while proj_budget[len(proj_budget)-i-1].isdigit()==True:
		i+=1
		higher_budget.append(proj_budget[len(proj_budget)-i])			

	lowerBudget = ''.join(lower_budget)
	higherBudget = ''.join(higher_budget)
	higherBudget = higherBudget[::-1]
	p=['0','0','']
	my_cost = '999'
	with open("budget.csv","r") as f:
		row = csv.reader(f)
		for r in row:
			if higherBudget > p[0] and higherBudget < r[0]:
				my_cost = r[1]
				break
			p = r	
	print "----------------------------------------"
	print "higherBudget : ",higherBudget
	print "my cost : ", my_cost
	time.sleep(1)
	try:
		inputCost = driver.find_element_by_class_name("earnedSum")
		
	except:
		inputCost = driver.find_element_by_class_name("earnedSum")

	inputCost.clear()
	inputCost.send_keys(my_cost)
	print "cost Entered"
	
	try:
		inputPeriod = driver.find_element_by_class_name("period")
	except:
		print "could not enter the time period"
	inputPeriod.clear()
	inputPeriod.send_keys("7")
	print "duration entered"
	print "----------------------------------------"

	flag=0
	while flag==0:
		print "\nclick place bid"
		driver.find_element_by_id("place-bid").click()

		try:
			driver.find_element_by_class_name("LiteModal-cancelAction").click()
			flag=1
		except:
			print "element not found"
			driver.execute_script("window.scroll(0,50)")
			time.sleep(0.4)
			flag=0


	#driver.find_element_by_id("place-bid").click()
	#time.sleep(0.8)
	#try:
	#	driver.find_element_by_id("place-bid").click()
	#except:
	#	print "operation already performed"

	#time.sleep(1)
	#try:
	#	driver.find_element_by_class_name("LiteModal-cancelAction").click()
	#except:
	#	print "element not found"
	#	sys.exit()

	prop = open("proporsal","r")
	proporsal = prop.readlines()
	try:
		inputProporsal = driver.find_element_by_id("proposalDescription")
	except:
		print "try other"
		inputProporsal = driver.find_element_by_class_name("BidProposal-form-textarea")

	time.sleep(1)
	inputProporsal.clear()
	inputProporsal.send_keys(str(proporsal).replace("[","").replace("]",""))
	driver.find_element_by_id("place-bid-step2").click()
	try:
		driver.find_element_by_id("place-bid-step2").click()
	except:
		pass
	time.sleep(1)

i=0
while True :
	print link
	driver.get(link)

	page_source = driver.page_source
	#print page_source
	file_src = open("page_source.html","w")
	fp = page_source.encode('utf-8')
	file_src.write(fp)
	

	html_page = open("page_source.html","r")
	soup = BeautifulSoup(html_page)
	link_file = open("link_final","a+")
	for link in soup.findAll('a', attrs={'href': re.compile("^https://www.freelancer.com/projects/")}):
    	print link.get('href')
    	link_file.write(link.get('href'))
	
	with open("links_final","r") as links:
		c = links.readlines()

	#for i in range(0,len(c)):
	while True:
		try:
			s = c[i]
			s =s.replace("\n","")
			operation_main(s)
			i+=1
		except:
			print "end of file"
			break