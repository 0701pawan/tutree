lst=list(map(int,input("Enter the elements in list ").split(" ")))
k=int(input("Enter the value of K "))
lst2=[]
for i in range (len(lst)-k):
    max1=lst[i]
    for j in range (i,i+k):
        if lst[j]>max1:
            max1=lst[j]
    lst2.append(max1)
print(lst2)