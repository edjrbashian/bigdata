import re
import urllib2


def getImageLocation():
  with urllib2.urlopen('http://apod.nasa.gov/apod/astropix.html') as h:
    # (?<=...) means "Matches if the current position in the string 
    #                 is preceded by a match for ... 
    #                 that ends at the current position."
    loc = re.search('(?<=IMG SRC=")image/\d+/[\w\d_]+.jpg', a).group()
  return 'http://apod.nasa.gov/apod/' + loc
  imgurl = 'http://apod.nasa.gov/apod/' + loc
  print imgurl
getImageLocation()