def afficheFichier(fich):
#     fich1 = open(fich,"w")
#     fich1.write("fatiha")
#     fich1.close()
    fich1 = open (fich , "r")
    return(fich1.read())
nom = "fichier.txt"
fic = open( "fichier.txt" , "w")
fic.write("je suis fatiha , j'ai 18 , Je suis une Etudiant ")
fic.close()
afficheFichier(nom)
