import urllib2
import ctypes
from HTMLParser import HTMLParser
import webbrowser
import urllib

# Grab image url
response = urllib2.urlopen('http://apod.nasa.gov/apod/astropix.html')


html = response.read()

class MyHTMLParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   #check url for proper format
                    if value.startswith("image/"):
                      if value.endswith("jpg"):
                        self.output=value

parser = MyHTMLParser()
parser.feed(html)
imgurl='http://apod.nasa.gov/apod/'+parser.output
file_name = imgurl.split('/')[-1]


# Save the file

output_folder = '/Users/edjrbash/Desktop/Big_Data/Media/'
urllib.urlretrieve(imgurl, output_folder + file_name)
print(file_name + " Downloaded")
