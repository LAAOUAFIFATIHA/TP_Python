import numpy as np 
for i in range(100,1000,1):
    y= str(i)
    a= int(y[0])
    b= int(y[1])
    c= int(y[2])
    if(not(a*b*c)==0):
                  if(( (a*b*c)%(a+b+c))==0):   
                            print (i) 