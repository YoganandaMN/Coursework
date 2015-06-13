import urllib2
from bs4 import BeautifulSoup
def main():
    def con(contact_us):
        opener=urllib2.build_opener()
        opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
        response=opener.open(contact_us)
        soup=BeautifulSoup(response)
        print ("COntact Information")
        for div in soup.findAll("div",{'class':'inner-content-box with-widgets'}):
            print div.get_text()
            #pass



    def forbidden403Error():
        url="http://plainsboronj.com/"
        opener=urllib2.build_opener()
        opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
        response=opener.open(url)
        soup=BeautifulSoup(response)

        print "Contact"
        for link in soup.findAll('a',{'id':"btn-contact-us"}):
            contact=link.get('href')
            contact_us=str(url+contact)

            con(contact_us)


        print ("plainsboronj Address")
        for add in soup.findAll("div",{'id':'address'}):
            print (add.get_text().encode('utf-8'))




        print ("Departsments" +" "+"are")

        #addrs(soup)
        for link in soup.findAll("li",{'class':'header'}):
            #print ("Departsments" +" "+"are")
            print link.get_text()

        #print response.read()

        #def addrs(soup):



    forbidden403Error()
if __name__ == '__main__':
    main()

