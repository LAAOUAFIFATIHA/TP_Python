def remp():
    dic = {}
    n = int(input("Combien de personnes voulez-vous ajouter : "))
    for i in range(n):
        nom = input("Donnez le nom : ")
        age = int(input("Donnez l'âge : "))
        taille = float(input("Donnez la taille : "))
        dic[nom] = ( age, taille)
    return dic 
def consol(dic):
       for cle,val in dic.items() :
               print("le nom :{} l'age:{} la taille:{}".format(cle,val[0],val[1]))
#___________________teste____________________#
n=remp()
consol(n)