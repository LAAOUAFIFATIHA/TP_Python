personnes={'adam':[12,'marakech'],'noha':[18,'safi'],'nada':[19,'safi']}
per={'fatiha':[18,'essaouira']}
personnes.update(per)
ville=[]
for cle,val in personnes.items():
    ville.append(val[1])
    print(cle,"a",val[0],"la ville",val[1])
for i in range(len(ville)):
    print(ville[i],"l'accurrence",ville.count(ville[i]))
ville.sort()
print(ville)
personnes.pop('adam')
