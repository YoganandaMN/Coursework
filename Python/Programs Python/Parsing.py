#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Durga
#
# Created:     27-05-2015
# Copyright:   (c) Durga 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib2
from urllib2 import urlopen
import re

def main():
    try:
        url="http://www.sec.gov/edgar/searchedgar/companysearch.html"
        request=urllib2.Request(url)
        print "urlopened"
        handle=urllib2.urlopen(request)
        st=handle.read()
        print st

        try:
            print("inside Second Try")
            titles=re.findall(r'<title>(.*?)</title>',st)
            print("After Second Try")
            for title in titles:
                print("After Second Try For loop")
                print title



        except Exception, e:
          print str(e)







    except Exception, e:
        print str(e)

if __name__ == '__main__':
    main()
