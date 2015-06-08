id<-1:5
age<-c(21,23,54,43,30)
name<-c("yoga","nanda","Sandeep","Shivu","Ravi")
x<-data.frame(id,age,name)
m<-list("a",1,c(1,2),x)

#An Reference to the list variable
names(m)<-c("Char","Number","vector","DataFrame")
m[["Char"]]
length(m)

#For adding An Another List item
m[["SiterName"]]<-"Kavya"
length(m)
m
m[["Number"]]

