import urllib2
from bs4 import BeautifulSoup
url="http://www.carteret.net/content/2855/3390/default.aspx"
town=url.split('.')[1]
print town
opener=urllib2.build_opener()
print "Builded opener"
opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
print "added headers"
response=opener.open(url)
print "Took Response"
#Storing the Browser data to  variable
soup=BeautifulSoup(response)
#class="ContentTemp_Zebra"
data=soup.get_text().encode('utf-8')
#print data
delimiter="Daniel J. Reiman, Mayor"
delimiter1="Government"
aa2=(data.partition(delimiter)[1])
print aa2
aa=(data.partition(delimiter)[2])
#print aa
aa1=(aa.partition(delimiter1)[0])
print aa1
file=open('test.txt','a')
file.writelines(town)
file.writelines("\n")

file.writelines(aa2)
file.writelines(aa1)
file.close()

