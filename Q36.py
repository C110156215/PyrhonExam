T=int(input("幾筆資料: "))
for i in range(T):
    a=int(input("輸入"))
    b=int(input("輸入"))
    c=int(input("輸入"))
    d=int(input("輸入"))
    if d-c==c-b==b-a:
        ans=d+(d-c)
        print(str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(ans)+" ")
        print("此為等差數列")
    elif d/c==c/b==b/a:
        ans=d*(d/c)
        print(str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(round(ans))+" ")
        print("此為等比數列")
    else:
        print("不是等差也不是等比")