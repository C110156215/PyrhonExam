T=int(input("T個班級數量: "))
list1=[]
for i in range(T):
    a=int(input("輸入: "))
    list1.append(a)
list1.sort()
print(list1[T-1])