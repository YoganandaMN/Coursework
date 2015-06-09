id<-1:5
age<-c(21,23,54,43,30)
name<-c("yoga","nanda","Sandeep","Shivu","Ravi")

x<-data.frame(id,age,name)
nrow(x)
ncol(x)

dim(x)
names(x)[2]
head(x)
tail(x)

x<-data.frame(id,age,name)
x

data.matrix(as.matrix(x))

a<-c(1,"yoga")
b<-matrix(a,nrow=2,ncol=3)
b

