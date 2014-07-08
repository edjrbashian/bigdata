import re
import urllib2
from bs4 import BeautifulSoup




#response = urllib2.urlopen('http://apod.nasa.gov/apod/astropix.html')

#def getImageLocation():
#html = response.read()

soup=BeautifulSoup(open("http://apod.nasa.gov/apod/astropix.html"))
#print soup
#Id= soup.find("a")
#print Id
#print html
#for line in html:
	#print line,
#	if "< " in line: 


    # (?<=...) means "Matches if the current position in the string 
    #                 is preceded by a match for ... 
    #                 that ends at the current position."
    #loc = re.search('(?<=IMG SRC=")image/\d+/[\w\d_]+.jpg', a).group()
  #return 'http://apod.nasa.gov/apod/' + loc
  #imgurl = 'http://apod.nasa.gov/apod/' + loc
  #print imgurl
#getImageLocation()