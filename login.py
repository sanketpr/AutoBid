from selenium import webdriver
import pickle
import time

driver = webdriver.Firefox()
driver.get("https://freelancer.com")
time.sleep(20)
pickle.dump(driver.get_cookies(),open("cookies.pkl","w"))

driver.get("https://www.freelancer.com/dashboard/projects.php")

#i1297018
#marvel789
#cookies = pickle.load(open("cookies.pkl", "rb"))

#for cookie in cookies:
#    driver.add_cookie(cookie)

#driver.get("https://www.freelancer.com/jobs/myskills/1/")

#page_source = driver.page_source
#print page_source
#file_src = open("page_source.html","w")
#fp = page_source.encode('utf-8')
#file_src.write(fp)

