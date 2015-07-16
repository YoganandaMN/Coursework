import requests
import urllib2
from bs4 import BeautifulSoup
def main():
        url="http://plainsboronj.com/"
        opener=urllib2.build_opener()
        opener.addheaders=[('user-agent','Chrome/41.0.2243.0')]
        #opener.unicode=encode('utf-8')
        response=opener.open(url)
        print response
        soup=BeautifulSoup(response)
        for i in soup.findAll('a'):


            print (i.get('href'))
            buf=i.get('href')
            op=open("href.txt",'wb') #Creates File As a Company name
            p=op.write(buf)    #Writes the browser data into a file
            print ("\n")

            op.close()  #closes the fil
        print "href has been written"







if __name__ == '__main__':
    main()