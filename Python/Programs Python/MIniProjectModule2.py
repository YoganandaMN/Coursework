import urllib2
from bs4 import BeautifulSoup
import time
import xlrd
import re
import csv
import string
def Contact_Info():
                    datasets=[]
                    def ToGetItIn_manner(datasets):
                              count=0
                              print "Data Cleaning"
                              for p in datasets:
                                        count+=1
                                        print count
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
                                        #st4=st4.remove(' Email')
                                        st5=" ".join(st4.split())

                                        #print st5

                                        a=st5.split(",")
                                        #a=a.strip()

                                        if count==1:
                                                            data=['TownshipName','Departmenet','PhoneNo','Ext','fax']
                                                            file=open(TownshipName+".csv",'ab')
                                                            print "file opened"
                                                            file.write(str(data))
                                                            file.write("\n")
                                                            print "data is written"
                                                            file.close()
                                                            print data

                                        else:
                                                  try:

                                                            del a[1]
                                                            a.insert(0,TownshipName)
                                                            a.insert(2, phone)
                                                            if len(a)==6:
                                                                      del a[-2]
                                                                      file=open(TownshipName+".csv",'a')
                                                                      file.write(str(a))
                                                                      file.write("\n")
                                                                      file.close()
                                                                      print a
                                                            elif len(a)>6:
                                                                      del a[-1],a[-2],a[-3],a[3],a[4]
                                                                      file=open(TownshipName+".csv",'a')
                                                                      file.write(str(a))
                                                                      file.write("\n")
                                                                      file.close()
                                                                      print a
                                                            else:
                                                                      file=open(TownshipName+".csv",'a')
                                                                      file.write(str(a))
                                                                      file.write("\n")
                                                                      file.close()
                                                                      print a

                                                  except:
                                                            pass

                    def FetchThe_Data(table):
                              print "came inside fetch"

                              for row in table.find_all("tr"):
                                        dataset = row.get_text()#.encode('utf-8')
                                        #print dataset
                                        datasets.append(dataset)
                              ToGetItIn_manner(datasets)
                    url="http://www.oldbridge.com/content/137/default.aspx"
                    opener=urllib2.build_opener()
                    print "Builded opener"
                    opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
                    print "added headers"
                    response=opener.open(url)
                    print "Took Response"
                    #Storing the Browser data to  variable
                    soup=BeautifulSoup(response)
                    TownshipName=soup.find('div',{'class':'title'}).get_text().encode('utf-8')
                    #file=open(text+".csv",'a')
                    #file.write(text+"\n")

                    #print st5
                    TownshipName=TownshipName.lstrip()
                    print TownshipName
                    #class="grid_8 alpha omega"
                    text1=soup.find('div',{'class':'grid_8 alpha omega'})
                    phone=text1.find('h3').get_text().encode('utf-8')
                    phone=phone.split(':')
                    phone=phone[1].lstrip()
                    print phone
                    #file=open(text+".csv",'a')
                    #file.write(phone+"\n")

                    #print st5
                    print phone

                    CranburyTownship=soup.find('table',{'class':'ContentTemp_Directory'})
                    #'table',{'class' : 'ContentTemp_Directory'}

                    if CranburyTownship:

                              FetchThe_Data(CranburyTownship)

                    #ToGetItIn_manner(datasets,name,url)



Contact_Info()








