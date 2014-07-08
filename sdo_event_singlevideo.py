from datetime import date, timedelta
import urllib2
import ctypes
from HTMLParser import HTMLParser
import webbrowser

# this script downloads a specific SDO instrument's daily video 
#print yesterdays date
yesterday = date.today() - timedelta(1)
yesterday_date = yesterday.strftime('%Y/%m/%d/')
yesterday_date_url = yesterday.strftime('%Y%m%d')
print yesterday_date

#newest videos are from the day before
web_url = 'http://sdo.gsfc.nasa.gov/assets/img/dailymov/' + yesterday_date
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
                   if value.startswith(yesterday_date_url +'_1024_0171'):
                   #if name == "0193":
                    if value.endswith(".mp4"):
                       #print value
                       self.output=value
                       print value


parser = MyHTMLParser()
parser.feed(html)

#complete the link with the parser output
imgurl= web_url +parser.output



print imgurl



img = urllib2.urlopen(imgurl)
file_name= yesterday_date_url + "_0171.mp4"
localFile = open(file_name, 'wb')
localFile.write(img.read())
localFile.close()
print("File Downloaded")