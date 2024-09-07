import random
class jeuDeCartes:
    def __init__(self):
        self.liste=[(j,i) for i in range(4) for j in range(2,15)]
        
    def mon_carte(self,valeur,couleur):
        tab1=['2','3','4','5','6','7','8','9','10','valet','dame','roi','as']
        tab2=['coeur','careau','trefle','pique']
        for j,i in self.liste:
            if j==valeur and i==couleur:
                print("{} de {} ".format(tab1[int(j)-2],tab2[int(i)]))
        print(None)

    def methode_Battre(self):
        random.shuffle(self.liste)
        return(self.liste)
    def tirer(self):
        if len(self.liste)>0: 
            n=self.liste.pop(0)
            print("l'element reterer est :",n)
        else:
            print(" None")

jeu=jeuDeCartes()
print(jeu.liste)
jeu.methode_Battre()
#jeu.mon_carte(14,3)
for i in range(53):
      print("\nlist avant supp",jeu.liste)
      jeu.tirer()

