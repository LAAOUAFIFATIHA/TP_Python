import string
alph = string.ascii_letters


def cryptage(ch):
    res = ''
    for i in ch:
        if ch.count(i) % 2 == 0:
            k = ch.count(i)//2
        else:
            k = ch.count(i)*2
        res = res + alph[(alph.index(i) + k) % 26]
    return print(res)


cryptage("zz")


# td part two
# باسم الله


def copylist(listy):
    liste = [0] *len(listy)
    liste = [ i for i in listy ]
    return liste


listy =[1,2,3]
#copylist(listy)

def list_premier():
    list_new =[1] * 1000
    #list_new = [ 0  for i in range (2,1001)  if (i%2 ==0)or (i%3==0) ]
    for i in range (2,1000):
        if (i%2 ==0)or ((i%3==0) and  (i !=3)):
            list_new [i]= 0
    return print( list_new)

list_premier()
