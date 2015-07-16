import urllib2
from bs4 import BeautifulSoup
import time
import xlrd
import re
import string
def Contact_Info():
                    datasets=[]
                    def ToGetItIn_manner(datasets,name,url):
                              print "Data Cleaning"
                              for p in datasets:
                                        p=p.encode('ascii','ignore')
                                        p=str(p)
                                        p=p.splitlines()
                                        p=filter(None,p)
                                        p=list(p)
                                        ls=[]
                                        for st in p:
                                                  st1=st.strip('\t')
                                                  ls.append(st1)

                                        st=str(ls)
                                        st1=st.strip('[')
                                        st2=st1.strip(']')
                                        st3=st2.strip("'")
                                        st4=str(st3.replace("'", ""))
                                        st5=" ".join(st4.split())

                                        print st5

                    def FetchThe_Data(table,name,datasets,url):
                              print "came inside fetch"

                              for row in table.find_all("tr"):
                                        dataset = row.get_text()#.encode('utf-8')
                                        print dataset
                                        datasets.append(dataset)
                              ToGetItIn_manner(datasets,name,url)
                    url="http://www.piscatawaynj.org/pway/contacts/contact-us"
                    opener=urllib2.build_opener()
                    print "Builded opener"
                    opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
                    print "added headers"
                    response=opener.open(url)
                    print "Took Response"
                    #Storing the Browser data to  variable
                    soup=BeautifulSoup(response)
                    #Identifing_The_Data(soup,url)

                    CranburyTownship=soup.find('table',{'style':'border-collapse:collapse; color:rgb(0, 0, 0); font-family:verdana,arial,helvetica,sans-serif; width:100%'})#style="border-collapse:collapse; color:rgb(0, 0, 0); font-family:verdana,arial,helvetica,sans-serif; width:100%".yt{}/+
                    #'table',{'class' : 'ContentTemp_Directory'}
                    if CranburyTownship:
                              print "CranburyTownship mayor and council"
                              #print table.get_text()
                              FetchThe_Data(CranburyTownship,"CranburyTownship",datasets,url)

                    #ToGetItIn_manner(datasets,name,url)



Contact_Info()








