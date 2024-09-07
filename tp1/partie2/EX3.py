def crypt(ch,y):
    ch=ch.upper()
    alph='ABCDEFGHIJKLMNOPQSRTUVWXYZ'
    res=''
    for c in ch:
            if (alph.index(c)+y)>25:
                 res+=alph[y+((alph.index(c)-25)-1)]
            else:
                 res+=alph[alph.index(c)+y]
    print(res)
    
x='FaTTTTTZy'              
crypt(x,4)  