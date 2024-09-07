class voiture :
    def __init__(self,  marque='ford',couleur='rouge',pilot='personne',vitesse =0):
        self.marque = marque
        self.couleur = couleur 
        self.pilot = pilot
        self.vitesse = vitesse
    def choixconducteur(self,nom):
        self.pilot = nom
    def accelerer (self,taux,duree):
        if not self.pilot =='personne':
            self.vitesse=taux*duree
        else :
            print("tu peut pas changer la vitesse car le pilot est non definie")
    def affiche(self): 
        print("la marque ={} , la couleur = {} , pilot = {} vitesse ={}".format(self.marque,self.couleur,self.pilot ,self.vitesse))
        
        
        
p=voiture('firari','black','fatiha')
p.choixconducteur('fatiha') 
p.accelerer(22,99) 
p.affiche()      