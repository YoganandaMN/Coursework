#Vectors can be thought of as contiguous cells containing data. 
#Cells are accessed through indexing operations such as x[5]
vector<-c("character",1,2,33)
vector
 a<-1:10
a<5
any(a<5)
all(a<5)
a[3]
a[:2]
#used for initialising the vectors
c<-vector("numeric",length=10)
c

#Mixing the objecs

y<-c(1.7,"y")
y #Converts to Character

x<-c(TRUE,2)
x#Converts TO Number

x<-c("a",TRUE)
x#Converts TO Character
