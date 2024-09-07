class Donimo:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
        
    def affiche_point(self):
        return( "face A={} face B ={}".format(self.a , self.b))
    def valeur(self):
        return(self.a + self.b)
    def produit(self): 
        return (self.a*self.b)
         
d1 = Donimo(2,7)
d2 = Donimo(5,4)
d1.affiche_point()
print ( "total des points :",d1.valeur()+d2.valeur())
#print ("le produite :",d1.produit())
liste_Domino=[]
for i in range(7):
    for j in range(7):
       liste_Domino.append(Donimo(j,i))
for i in liste_Domino:
    print(i.affiche_point(),i.valeur())