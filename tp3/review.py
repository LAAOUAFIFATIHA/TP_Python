
# fonction qui retourne les diveiseurs communs entre deux nbr 
#fonction 

def diveseurs_communs(m , n):
    div_m = [ i  for i in range(1,m//2)  if m%i ==0 ]
    div_n = [ i  for i in range(1,n//2)  if n%i ==0 ]
    div_communs = [ i for i , j  in zip(div_m,div_n ) if j == i]
    return (div_communs)
m ,n = 20 , 10
#print(diveseurs_communs(m, n))


# fonction qui reoturne le plus grand nbr premier qui enférier  à un nbr
#fonction de nbr premier 
def nbr_premier (n) :
    list_p = [ i for i in range( 2,n) if n % i == 0]
    if len(list_p)==0:
        return True 
    else :
        return False
    
def plus_grand_nbr_prenier (n):
    list_premier = [ i for i in range (n+1) if nbr_premier(i)]
    if list_premier:
        return list_premier[-1]
    else:
        return (print("il n'y a auccun nbr premiers"))
    
#print(plus_grand_nbr_prenier(3))

# fonction qui vérifier si un nbr est distinct ou  non
#fonction

def nbr_distinct(n):
    str_nbr = str(n)
    for i in str_nbr:
        if str_nbr.count(i) > 1 :
            return (print("ce nbr n'est pas distinct "))
    return (print("ce nbr est distinct"))

#nbr_distinct(280)

#fontion qui vérifier les elemnet identique entre deux lists des elements
#fonction 


def element_semble(x , y):
    x1 = x.split()
    y1 = y.split()
    minlist = min((x1) , (y1))
    maxlist = max ((x1) , (y1))
    list_communs = [i for i in maxlist  if i in minlist]
    return (print(list_communs))
x = "Python est un langage de programmation" 
y = "Python est orienté objet un"

#element_semble(x, y)

#fonction qui donner le nbr les accurence de chaque nombre 
#fonctinon

def nbr_accurence (chaine) :
    res = ""
    acc = 1
    if len(chaine) < 50 :
        for i,j in enumerate (chaine) :
            if (i+1 < len(chaine)) and (j == chaine[i+1]):
                acc = acc + 1
            else :
                    res = res + str(acc) +j
                    acc = 1

    return print(res )
#nbr_accurence("ffftttikkw")

#fonction qui ordoner les elemenets d'une liste dans deux list depend de l'index si pair ou impair
#fonction

def organise(listy):
    l_even =[j for i, j in enumerate (listy)  if i%2 == 0]
    l_odd = [j for i,j in enumerate (listy) if i%2 != 0]
    return ((l_even,l_odd))
listy=["pair","imp","pair","imp","pair" ,"imp"]
#print(organise(listy))



#fonction qui donne un nombre dans une liste et leurs accurence 
#fonction

def count_accrrence(listy):
    list_accurrence = []
    for i in listy :
        if (i ,listy.count(i)) not in list_accurrence:
            list_accurrence.append((i,listy.count(i)))
    return list_accurrence

listy = [1,2,9,4,2,1]
count_accrrence(listy)

#fonction qui classifier les elements dans un dictionnaire à des positives et négatives 
#fonction
classeur={"Positif":[],"Negatif":[]}

def classifier(x):
    if x < 0 :
        classeur["Negatif"].append(x)
    else :
        classeur["Positif"].append(x)
    return classeur
classifier(8)
classifier(-6)
classifier(1)
classifier(-5)
classifier(-99)











