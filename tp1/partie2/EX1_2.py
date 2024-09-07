import string
def crypt(ch):
    ch=ch.upper()
    #alph='ABCDEFGHIJKLMNOPQSRTUVWXYZ'
    alph=string.ascii_uppercase
    res=''
    for c in ch:
        n=ch.count(c)
        if n%2==0:
            k=n//2
        else:
            k=n*2
        if (alph.index(c)+k)>25:
                 res+=alph[k+((alph.index(c)-25)-1)]
        else:
                 res+=alph[alph.index(c)+k]
    print(res)
x='tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttz'              
crypt(x)        
        
        
    
    
    
    
    
    
