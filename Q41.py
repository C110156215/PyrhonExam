T=int(input("搭了幾次電梯: "))
list1=[1]
sum=0
if 1<=T<=10:
    for i in range(T):
        a=int(input("輸入: "))
        list1.append(a)
    for i in range(T,0,-1):
        if (list1[i]-list1[i-1])>0:
            sum+=20*(list1[i]-list1[i-1])
        elif (list1[i]-list1[i-1])<0:
            sum+=10*(list1[i-1]-list1[i])
    print(str(sum)+" 元")


else:
    print("次數錯誤")