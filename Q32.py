ming=int(input("小明身上有幾元: "))
much=int(input("販賣機有幾種飲料: "))
lis=[]
total=0
if 100>=ming>=0 and 30>=much>=1:
    for i in range(much):
        a=int(input("輸入: "))
        lis.append(a)

    for i in range(much):
        if ming>=lis[i]:
            total+=1
    print(total)
else:
    print("輸入錯誤")
