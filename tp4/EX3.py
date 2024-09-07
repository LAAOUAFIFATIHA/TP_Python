class cercle:
    def __init__(self,rayon):
        self.rayon= rayon
    def surface(self):
        return (self.rayon**2*3.14)
class cylindre(cercle):
    def __init__(self,rayon,hauteur):
        super().__init__(rayon)
        self.rayon = rayon
        self.hauteur = hauteur
    def volume(self):
        return((self.rayon**2)*3.14*(self.hauteur))
x = cercle(6)
print(x.surface())
y = cylindre(2,3)
print(y.volume())