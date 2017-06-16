from bs4 import BeautifulSoup
import urllib2

#ask = input("Enter amount of pages you want: ")

#while ask != 0:
url = BeautifulSoup(urllib2.urlopen("https://en.wikipedia.org/wiki/Special:Random"),"html.parser")

filter_title = str(url.title)
filter_p = str(url.p)

print filter_title[7:filter_title.find(" - Wi")]
#print filter_p
for char in filter_p:
    if char == "<":
        filter_p.find("")
print filter_p
#ask = ask - 1

#ok lets come back to this later












