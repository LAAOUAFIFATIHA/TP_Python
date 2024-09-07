n = input("Entrer un nom : ")
voy = ["A", "E", "I", "O", "U", "Y"]
rang = [1, 5, 9, 15, 21, 25]
poid = 0
for i, c in enumerate(n,start=1):
    if c.upper() in voy:
        poid += i * rang[voy.index(c.upper())]
print(poid)

