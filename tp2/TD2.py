#__________________NBCMin_____________________#
def NBCMin(n):
    n=str(n)
    i=0
    for c in n:
        if(c.isalpha()&c.islower()):
            i+=1
    return(i)
#__________________NBCMij_____________________#
def NBCMij(n):
    n=str(n)
    i=0
    for c in n:
        if(c.isalpha()&c.isupper()):
            i+=1
    return(i)
#_________________NBCMialpha_________________#
def NBCMialpha(chaine):
    i=0
    for c in chaine:
        if not c.isalpha():
            i+=1
    return(i)
#_________________longMAJ_________________#
def longmaj(n):
    s = ""
    list_s = []
    for c in n:
        if  c.isupper():
            s += c
        else:
            if s:
                list_s.append(s)
            s = ""
    if s:
        list_s.append(s)
    resultat = max(list_s, key=len)
    return len(resultat)
#_________________longMin_________________# 
def longmaj(n):
     s = ""
     list_s = []
     for c in n:
         if  c.islower():
             s = c + s
         else:
             if s:
                 list_s.append(s)
             s = ""
     if s:
         list_s.append(s)
     resultat = max(list_s, key=len)
     return len(resultat)           
    #_________________longMin_________________#     
    
def longmin(n):
    s = ""
    list_s = []
    for c in n:
        if c.islower():
            s = c + s
        else:
            if s:
                list_s.append(s)
            s = ""
    if s:
        list_s.append(s)
    resultat = max(list_s, key=len)
    return len(resultat)
         #_________________score_________________#
def score(n):
    som_bous=len(n)*4+(len(n)-NBCMij(n))*2+(len(n)-NBCMin(n))*3+NBCMialpha(n)*5
    pen=longmin(n)*2+longmaj(n)*2
    res=som_bous- pen
    print("le score est :",res)
    if(res<20):
        print("le mot de passe est tres faible")
    else:
        if(res<40):
            print("le mot de passe est  faible")
        else:
            if(res<80):
                print("le mot de passe est fort")
            else:
                print("le mot de passe est tres fort")
                
                
                
l="fatiha@laaouafi2005"                
score(l)



"""___________________________la corriction de td_2_______________________                   
    
def NBCMin(pas):
    return sum([1 for i in pas if i.islower()])
def NBCMij(pas):
    return sum([1 for i in pas if i.isupper()])
def NBCALpha(pas):
    return sum([1 for i in pas if  not i.isalpha()])"""
  
    
    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    