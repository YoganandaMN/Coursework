#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Durga
#
# Created:     28-05-2015
# Copyright:   (c) Durga 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib2
import webbrowser
import BeautifulSoup
def main():
     company=raw_input("enter the companey name")
     request=urllib2.Request("//www.sec.gov/cgi-bin/browse-edgar?company="+company+"&owner=exclude&action=getcompany")
     #web
     print "urlopened"
     handle=urllib2.urlopen(request)
     soup=BeautifulSoup(handle)

     for link in soup.find_all('a'):
        print(link.get('href'))
if __name__ == '__main__':
    main()
