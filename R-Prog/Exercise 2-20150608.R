#Redo the previous exercise a more efficient way, i.e., without using a for loop.
#(Hint: Using sample and matrix, this can be done in just two lines.)
v<-c(1:20)
length(v)
m<-matrix(sample(length(v),20,replace = FALSE),nrow=10,ncol=2)
m
