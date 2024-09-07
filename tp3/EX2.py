def copy_to_other(fichier1 , fichier2):
    f1 = open(fichier1 , "r")
    for c in f1 :
        f2 = open (fichier2 , "w")
        f2.write(c.upper())
        f2.close()
    f1.close()
    
fichier1 = "fichier.txt"
fichier2 = "fichier2.txt"
copy_to_other(fichier1 ,fichier2)
n = open ("fichier2.txt" ,"r")
print(n.read())