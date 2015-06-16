import urllib2
from bs4 import BeautifulSoup
def main():
    def conT_Info(contact_us):
        #fetches Contact Information From the Contacts
        opener=urllib2.build_opener()
        opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
        response=opener.open(contact_us)
        soup=BeautifulSoup(response)
        print ("Contact Information")
        for div in soup.findAll("div",{'class':'inner-content-box with-widgets'}):


            y=div.get_text().encode('utf-8')
            print(div.get_text().encode('utf-8'))
            print len(y)
            #print y[0]
            #buf=i.get('href')
            op=open("plains.txt",'w') #Creates File As a Company name
            p=op.writelines(y+"\n")    #Writes the browser data into a file
            print ("\n")
            #a = div.findAll('a')[1]
            #print a.text.strip(), '=>', a.attrs['href']






    def forbidden403Error():
        url="http://plainsboronj.com/"
        opener=urllib2.build_opener()
        opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
        response=opener.open(url)
        soup=BeautifulSoup(response)

        #print "Contact"
        for link in soup.findAll('a',{'id':"btn-contact-us"}):
            contact=link.get('href')
            contact_us=str(url+contact)

            conT_Info(contact_us)
    forbidden403Error()

if __name__ == '__main__':
    main()
