

import urllib2
from bs4 import BeautifulSoup
def main():

          url="http://www.cranburytownship.org/"
          opener=urllib2.build_opener()
          opener.addheaders=[('user-agent','Chrome/41.0.2243.0')]
          response=opener.open(url)
          y=["Contact Us","Contacts","Phone-Email List"]
          soup=BeautifulSoup(response)
          for i in soup.findAll('a'):
                    #buf=str(i)
                    if any(x in i for x in y ):
                              href=i.get('href')
                              print href
'''
                              buf=str(i)
                              print (i)

                              op=open("href.txt",'a') #Creates File As a Company name

                              op.writelines(buf+"\n")    #Writes the browser data into a file
                              print ("\n")

'''
if __name__ == '__main__':
    main()
