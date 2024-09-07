def add_elements(fichier1 , fichier2):
    f1 = open(fichier1 , "r")
    f11 = list(f1)
    f1.close()
    f2 = open (fichier2 , "r")
    f22 = list(f2)
    f2.close()
    f22= [c for c in f11]
    for d in f22 :
        f2 = open (fichier2 , "a")
        f2.write(d)
        f2.close()
    n = open (fichier2 ,"r")
    print(n.read())
    
fichier1 = "fichier1.txt"
# n1 = open ("fichier1.txt" ,"w")
# n1.write("fatiha ")
# n1.close()
# n = open ("fichier3.txt" ,"w")
# n.write("first ")
# n.close()
fichier3 = "fichier3.txt"
add_elements(fichier1 ,fichier3)

