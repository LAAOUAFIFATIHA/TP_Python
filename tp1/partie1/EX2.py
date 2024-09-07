
n=int(input("donner  un nbr :"))
str_n=str(n)
for j in range(,n+1):
          str_j=str(j)
          som_j=0
          for i in range(len(str_j)):
                 som_j+=int(str_j[i])
          if(j + som_j==n):
                resultat=" n'est pas un auto-nomber " 
                break
          else:
               resultat="est un auto-nomber "
print(resultat)