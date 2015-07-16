'''
import urllib
htmlfile = urllib.urlopen("http://www.co.middlesex.nj.us/Government/Directory/Pages/directory.aspx")
htmlraw = htmlfile.read()
print htmlfile 
'''

import urllib

import mechanize
FH=open("bpk.txt",'a')
baseurl = "http://www.co.middlesex.nj.us"
url = "http://www.co.middlesex.nj.us/Government/Directory/Pages/directory.aspx"
b = mechanize.Browser()
b.open(url)
for link in b.links():
	#print link.url
	#a = link.url
	#FH=open("bpk.txt",'w')
	FH.writelines(baseurl+"/"+link.url+"\n\n")                   #appending url  to baseurl to get ultimate limk
	
FH.close()


	
	