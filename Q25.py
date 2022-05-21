a=input("請輸入考試次數及學生數: ")
p=input("每次考試所佔的比率: ")
b=a.split(" ")
d=p.split(" ")
n=int(b[0])
m=int(b[1])
sum=0
for i in range(m):
    c=input()
    e=c.split(" ")
    for j in range(n):
        sum+=float(e[j])*float(d[j])
sum/=m
print("全班總平均為: "+str(round(sum,2)))