a=input("假設答案為: ")
b=1
if len(a)>=5:
    print("限四位數")
else:
   
    while b!=0:
        b=input("輸入: ")
        A=0
        B=0
        for i in range(4):
            for j in range(4):
                if a[i]==b[j]:
                    if i==j:
                        A+=1
                    else:
                        B+=1
        print(str(A)+"A"+str(B)+"B")
        if A>=4:
            print("答對了")
            break
    