def nbrPremier(n):
    if(n<=1):
        return 0
    else:
         for i in range (2,n):
             if n%i==0:
                 return 0
    return 1
listy=[1]*1000
for i in range (2,1000):
    listy[i]=nbrPremier(i)
print(listy)

for i in range(1,1000):
    if listy[i]==1:
        print(listy.index(listy[i],i,1000))