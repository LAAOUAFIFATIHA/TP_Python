
n=input("donner un nbr :")
s=0
for i in range(len(n)):
    s+=int(n[i])
while(s>=10):
    str_s=str(s)
    s=0
    for i in range(len(str_s)):
        s+=int(str_s[i])
res=str(s)+n
print(res)