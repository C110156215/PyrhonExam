fre=int(input("輸入筆數n: "))
pi=["金","銀","銅","優"]
list1=[]
for i in range(4):
    a=int(input(pi[i]))
    if a>fre:
        a=fre
    list1.append(a)
for i in range(4):
    print(str(pi[i])+"牌得到"+str(list1[i])+"面")