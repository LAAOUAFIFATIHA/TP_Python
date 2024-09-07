#_________fonction de nbr premier________________#
def nbrPremier(n):
    res="True"
    if(n<=1):
        res="False"
    else:
         for i in range (2,len(str(n))+1):
             if n%i==0:
                 res="False"
                 break
         return(res)
#_________fonctin nbr circulaire________________#
def nbrcirculaire(n):
    n=str(n)
    nlist = list(n)
    for j in range(len(n)):
        if (nbrPremier(int(''.join(nlist)))=="True"):
            res="True"
        else:
                 res="False"
                 break
        nlist = nlist[j+1:] + nlist[:j+1]
    return(res)
#_________test de programme________________#
p=int(input("donner le premier nombre :"))
q=int(input("donner la deuxiemme nombre :"))
i=p
while(i<=q):
    if(nbrcirculaire(i)=="True"):
        print(i)
    i+=1