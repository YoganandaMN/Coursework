#Exercise 4: Redo the previous exercise a more efficient way, i.e., without using a for loop.
#(Hint: This may be a bit more challenging than it looks; you have to think outside the box.)
RandomGeneration<-function(){
  count<-1
  while(count<=10){
    n<-runif(10,min=-50,max=50)
    print(n)
    cat("\n")
    s<-sort.int(n)
    print(s)
    cat("\n")
    midpoint=(s[1]+s[10])/2
    mid<-"midpoint="
    cat(mid,midpoint,"\n")   
    cat("\n")
    count=count+1
  }
}
