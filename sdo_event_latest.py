from datetime import date, timedelta
import urllib2
import ctypes
from HTMLParser import HTMLParser
import webbrowser
import urllib

# this script downloads a specific SDO instrument's daily video 
#print yesterdays date
yesterday = date.today() - timedelta(1)
yesterday_date = yesterday.strftime('%Y/%m/%d/')
yesterday_date_url = yesterday.strftime('%Y%m%d')
print yesterday_date

#newest videos are from the day before
web_url = 'http://sdo.gsfc.nasa.gov/gallery/potw/latest' 
print web_url

response = urllib2.urlopen(web_url)
#print response
html = response.read()
#print html


class MyHTMLParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   #if value[len(value)-3:len(value)]=="jpg":
                   if value.endswith('best.mov'):
                       #print value
                       self.output=value
                       print value


parser = MyHTMLParser()
parser.feed(html)

#complete the link with the parser output
imgurl= 'http://sdo.gsfc.nasa.gov/' +parser.output
print imgurl
file_name= imgurl.split('/')[-1]
output_folder = '/Users/edjrbash/Desktop/Big_Data/Media/'
urllib.urlretrieve(imgurl, output_folder + file_name)

#img = urllib2.urlopen(imgurl)

#localFile = open(file_name, 'wb')
#localFile.write(img.read())
#localFile.close()
print("File Downloaded")