from BeautifulSoup import BeautifulSoup
import urllib2
import re

html_page = open("page_source.html","r")
soup = BeautifulSoup(html_page)
with open("link_final","a+") as link_file:
	c = link_file.readlines()
link_file.close()
link_file = open("link_final","a+")
try:
	for link in soup.findAll('a', attrs={'href': re.compile("^https://www.freelancer.com/projects/")}):
		flag="ok"
		for i in range(0,len(c)):
			if link.get('href') in c[i]:
				flag="no"
				break
		if flag=="ok":
			print link.get('href')
			link_file.write(link.get('href')+"\n")
except:
	print ""