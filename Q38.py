n=int(input("可能跑到的n個地方"))
a=[]
if 2<=n<=10:
    for i in range(n):
        b=int(input("輸入: "))
        a.append(b)
    for i in range(n):
        if a[i]%9==0 or a[i]%11==0:
            print("第"+str(i+1)+"個點 "+str(a[i]))
else:
    print("請輸入正確範圍")