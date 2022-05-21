a=int(input("組數為: "))
b=a
num=1
while a!=0:
    if num<=b:
        c=input("第"+str(num)+"組: ")
        d=c.split(" ")
        sum=(int(d[0])*250)+(int(d[1])*175)
        print("第"+str(num)+"組應收費用: "+str(sum))
        num+=1
        a-=1
    else:
        break