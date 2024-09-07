def revAlpha(CH):
    CH=CH.upper()
    res=''
    alpha='ABCDEFGIHJKLMNOPQSTUVWYZ'
    for c in CH:
        if c=='Z':
             res+='A'
        else:
            res+=alpha[alpha.index(c)+1]
    print(res)
            
ris =input ("donner une chaine de caractere :")
revAlpha(ris)

        
       
        
        
        
        
    