def remp(nom,age,taille):
    dic={}
    #for cle,val in dic.items() :
    dic[nom]=(age,taille)
    return dic
def CERCHER(dic,nom):
       for cle,val in dic.items() :
           if cle==nom:
               print("le nom :{} l'age:{} la taille:{}".format(cle,val[0],val[1]))

def consol(dic):
       for cle,val in dic.items() :
               print("le nom :{} l'age:{} la taille:{}".format(cle,val[0],val[1]))
        
        
#_________test_____________#
nom=input("donner le nom :")
age=int(input("donner l'age :"))
taille=float(input ("donner la taille :"))
dic={}
dic(remp(nom,age,taille))
consol(dic)



