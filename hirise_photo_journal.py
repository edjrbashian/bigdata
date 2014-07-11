from datetime import date, timedelta
import urllib2
import ctypes
from HTMLParser import HTMLParser
import webbrowser
import urllib
from BeautifulSoup import BeautifulSoup
#this script will aim to download 100 most recent MRO Hirise photo journal additions


#particular location of url
web_url = 'http://photojournal.jpl.nasa.gov/mission/MRO?subselect=Instrument%3AHigh+Resolution+Imaging+Science+Experiment+%28HiRISE%29%3A' 
#sanity check
print "Root  " + web_url

response = urllib2.urlopen(web_url)
html = response.read()
#create text file for file descriptions
my_file=open("file_name.txt", "w")

#make a list for raw parsed information
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

#initiate parser and feel it html                 
parser = MyHTMLParser()
parser.feed(html)

# sanity check
number_of_files = len(list_of_value)

#empty list for file name descriptions
descriptions=[]

#complete the link with the parser output
for i in list_of_value:
  imgurl = "http://photojournal.jpl.nasa.gov" + i
  file_name = i.split('/')[-1]
  #useful for next part
  url_suffix= file_name.split('.')[-0]
  output_folder = '/Users/edjrbash/Desktop/Big_Data/Media/Hirise/'
  #branch to each picture's html page to recover Description information
  page = urllib2.urlopen('http://photojournal.jpl.nasa.gov/catalog/'+url_suffix)
  #use beautiful soup plugin to parse description information from page
  soup = BeautifulSoup(page)
  x = str(soup.body.find('b'))
  #strip off extra html synthax 
  y = x.split(':  ')[-1]
  yy = y.split('<')[-0]
  descriptions.append(yy)
  print yy
  #download image and name it as description 
  urllib.urlretrieve(imgurl, output_folder +yy+".jpg")
  #create a text document that has a list of all file names for refrence.
  my_file.write("%s\n" % yy)

my_file.close()

print("Hirise Successfully Downloaded "+str(number_of_files)+" files")
print ("Number of descriptions Counted " +str(len(descriptions)))


  