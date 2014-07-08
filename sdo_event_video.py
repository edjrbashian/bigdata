from datetime import date, timedelta
import urllib2
import ctypes
from HTMLParser import HTMLParser
import webbrowser
import urllib

#this script will aim to download all SDO instrument videos ending with .mp4 
#print yesterdays date
yesterday = date.today() - timedelta(1)
yesterday_date = yesterday.strftime('%Y/%m/%d/')
yesterday_date_url = yesterday.strftime('%Y%m%d')
print "Yesterdays Date: " +yesterday_date

#newest videos are from the day before
web_url = 'http://sdo.gsfc.nasa.gov/assets/img/dailymov/' + yesterday_date
print "Root  " + web_url

response = urllib2.urlopen(web_url)
#print response
html = response.read()
#print html

list_of_value = []
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                #only download mp4 files
                    if value.endswith(".mp4"):
                       list_of_value.append(value)
                       self.output=value
                       
parser = MyHTMLParser()
parser.feed(html)

#complete the link with the parser output
for i in list_of_value:
  
  imgurl = web_url + i
  file_name=  i
  output_folder = '/Users/edjrbash/Desktop/Big_Data/Media/'
  urllib.urlretrieve(imgurl, output_folder + file_name)
  print(i + "   File Downloaded")
print("Job Complete")