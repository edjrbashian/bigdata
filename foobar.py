import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('http://photojournal.jpl.nasa.gov/catalog/PIA18399')
soup = BeautifulSoup(page)

x = soup.body.find('b')
#x = soup.body.find('div', attrs={'class' : 'container'})
print x