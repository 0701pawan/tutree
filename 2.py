string=input()
head=0
end=len(string)-1
while head<=end:
    if string[head]==string[end]:
        head=head+1
        end=end-1
    else:
        print("not pallindrome")
        break
if head>end:
    print("is pallindrome")

