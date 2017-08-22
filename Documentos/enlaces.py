import urllib2
import re

url = ("http://deletesql.com/viewtopic.php?f=5&t=24")
html = urllib2.urlopen(url).read()
direcciones = re.findall('href="(http://.*?)"',html)


for urls in direcciones:
    print urls
