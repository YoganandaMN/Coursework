functionNames<-function(){
          #This is for vectors
          x<-1:3
          x
          #Assigning names to Column
          names(x)<-c("yoga","nanda","yogi")
          x
          names(x)
          #To access the value using name
          x["yoga"]
          x[2]
          
}

functionNames1<-function(){
          #This is for list, List can also have name
          y<-list("id"=A112,Name="yogananda",Location="Bangalore")
          y
          
          class(y)
          #To access the particular value
          y[["id"]]
}

functionNames2<-function(){
          #maatrix can have both Row and Column names
          m<-matrix(1:4,nrow<-2,ncol<-2)
          #Providing Column names Using DIMNAMES and List
          dimnames(m)<-list(c("a","b"),c("c","d"))
          m
          #Other way is using COLNAMES and ROWNAMES
          colnames(m)<-c("e","f")
          rownames(m)<-c("g","h")
          m
          
          
          
}