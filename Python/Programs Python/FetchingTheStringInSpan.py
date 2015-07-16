import requests
import urllib2
from bs4 import BeautifulSoup
def main():
        url="http://www.flipkart.com/"
        request=urllib2.Request(url)
        print "urlopened"
        handle=urllib2.urlopen(request)
        soup=BeautifulSoup(handle)
        for link in soup.findAll('span'):
            print (link.string)



if __name__ == '__main__':
    main()