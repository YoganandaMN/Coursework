#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Durga
#
# Created:     16-06-2015
# Copyright:   (c) Durga 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib2
from bs4 import BeautifulSoup

def main():
          url="http://www.co.middlesex.nj.us/Government/Departments/CS/Pages/County%20Clerk/County-Clerk.aspx"
          opener=urllib2.build_opener()
          opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
          response=opener.open(url)
          soup=BeautifulSoup(response)

          for add in soup.findAll("div",{'class':'contact-info'}):
                    print (add.get_text().encode('utf-8'))

if __name__ == '__main__':
    main()
