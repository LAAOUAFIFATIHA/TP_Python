import random
def nbrAleatoire(to,m):
    listy=[]
    for i in range(m-1):
        nbr_a=random.randint(1,to-sum(listy)-(m-1-len(listy)))
        listy.append(nbr_a)
    listy.append(to-sum(listy))
    return(listy)

n=int(input("donner le nbr de valeur a tirer au hasard (default=1000) :"))
M=int(input("donner la fractions pour partager l’intervalle (par default =5):"))
while M<2 or M>int(n)/10:
      M=input("donner la fractions pour partager l’intervalle (par default =5):")
print("tirage au sort les {} valeur".format(n))
liste=nbrAleatoire(n,M)
print("les valeur tirer sont :",liste)
list_fra=[]
for i in range(len(liste)):
    list_fra.append(liste[i]/n)
print("la fraction des valeur tirer successivement....")
print(list_fra)