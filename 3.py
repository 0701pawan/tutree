lst=list(input().split(" "))
dlst=[]
for i in range (len(lst)):
    if dlst.count(lst[i])==0:
        dlst.append(lst[i])
        print(lst[i],end=" ")