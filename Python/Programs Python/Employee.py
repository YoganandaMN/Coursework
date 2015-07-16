import re

n=['Vincent Asciolla', ' Councilman ', ' 51 Main Street', ' Helmetta', ' NJ 08828', ' Tel: 732-521-4946']
for data in n:
          y=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',data)
          if y:
                    print y.group()
          else:
                    pass


          '''
x=re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',n)
print x.group()
y=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',n)
print y.group()
'''