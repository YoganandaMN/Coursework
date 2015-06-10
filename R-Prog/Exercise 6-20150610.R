
DoorFun<-function(){
          n=100
          #Intiially all the Doors are opened 1opened 0closed
          vec<-rep(0,100)#Generates 100 Zeros means all the doors are closed
          cat ("initial Doors are closed\n")
          print (vec)
          for(i in 1:100){
                    
                    #print (vec[i])
                    #Checks the doors based on sequenced crated
                    for(j in seq(i,n,i) ){#if i is 2 seq will be 2,4,6,8...100
                              
                              if(vec[j]==1){
                                        vec[j]=0 #close door
                              }else{
                                        vec[j]=1 #opens door
                              }
                              
                    }
                    
                    
                    #print(i)
                    
          }
          cat ("Final Position of the doors\n")
          print (vec)
          print("o=close 1=open")
          
}
