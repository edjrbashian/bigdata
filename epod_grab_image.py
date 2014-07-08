import urllib2
import ctypes
from HTMLParser import HTMLParser
import webbrowser
import urllib

# Grab image url

response = urllib2.urlopen('http://epod.usra.edu/index.html')

html = response.read()

class MyHTMLParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   #if value[len(value)-3:len(value)]=="jpg":
                   if value.startswith("http://epod.usra.edu/"):
                    if value.endswith("-pi"):
                       #print value
                       self.output=value
                       

parser = MyHTMLParser()
parser.feed(html)
imgurl=parser.output
file_name = imgurl.split('/')[-1]

# Save the file Old Way
#img = urllib2.urlopen(imgurl)
#localFile = open(file_name, 'wb')
#localFile.write(img.read())
#localFile.close()
#print("File Downloaded")
# Save the file

#Save the file
output_folder = '/Users/edjrbash/Desktop/Big_Data/Media/'
urllib.urlretrieve(imgurl, output_folder + file_name)
print(file_name + " Downloaded")