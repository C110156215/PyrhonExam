a=input("甲方的數字: ")
b=input("乙方的數字: ")
end=[]

if len(a)==len(b):
    for i in range(len(a)):
        top=int(a[i])
        down=int(b[i])
        if top==1 and down==5:
            end.append("贏")
        elif top==5 and down==1:
            end.append("輸")
        elif top==down:
            end.append("和")
        elif top>down:
            end.append("贏")
        elif top<down:
            end.append("輸")
    print("洗刷刷結果: ",end="")
    for i in range(len(a)):
        print(end[i],end="")
else:
    print("輸入不相等")
