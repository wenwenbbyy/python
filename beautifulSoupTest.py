import urllib
from bs4 import *

url=raw_input('Enter - ')
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html,"html.parser")

tags=soup('a')
for tag in tags:
	print 'TAG:',tag
	print 'URL:', tag.get('href',None)
	print 'Content:',tag.contents[0]
	print 'Attrs:',tag.attrs