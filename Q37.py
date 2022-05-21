n=int(input("輸入n(0<n<1,000,000): "))
list1=[]
list1.append(n)
while n!=1:
    if n%2==1:
        n=(n*3)+1
        list1.append(round(n))
    else:
        n=n/2
        list1.append(round(n))
print("數列: ",end="")
for i in range(len(list1)):
    print(str(list1[i])+" ",end="")