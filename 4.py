string=input()
ul=[]
ll=[]
nl=[]
pl=[]
for a in string:
    if a.islower():
        ll.append(a)
        pl.append('l')
    elif a.isupper():
        ul.append(a)
        pl.append('u')
    elif a.isdigit():
        nl.append(a)
        pl.append('n')

ul.sort()
ll.sort()
nl.sort()
k=0
p=0
o=0
for a in pl:
    if a=='l':
        print(ll[k],end="")
        k=k+1
    elif a=='u':
        print(ul[p],end="")
        p=p+1
    else:
        print(nl[o],end="")
        o = o + 1

