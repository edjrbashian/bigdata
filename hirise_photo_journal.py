from datetime import date, timedelta
import urllib2
import ctypes
from HTMLParser import HTMLParser
import webbrowser
import urllib
from BeautifulSoup import BeautifulSoup
#this script will aim to download all SDO instrument videos ending with .mp4 


web_url = 'http://photojournal.jpl.nasa.gov/mission/MRO?subselect=Instrument%3AHigh+Resolution+Imaging+Science+Experiment+%28HiRISE%29%3A' 
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
                    if value.endswith(".jpg"):
                       list_of_value.append(value)
                       self.output=value
                       
parser = MyHTMLParser()
parser.feed(html)
number_of_files = len(list_of_value)

#complete the link with the parser output
for i in list_of_value:

  imgurl = "http://photojournal.jpl.nasa.gov" + i
  file_name = i.split('/')[-1]
  #file_name=  i
  output_folder = '/Users/edjrbash/Desktop/Big_Data/Media/Hirise/'
  urllib.urlretrieve(imgurl, output_folder + file_name)
  print(file_name+ "   File Downloaded")
print("Hirise Successfully Downloaded "+str(number_of_files)+" files")