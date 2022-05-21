fre=int(input("輸入筆數n: "))
dict1={"金":0,"銀":0,"銅":0,"優":0,}
a=int(input("金"))
b=int(input("銀"))
c=int(input("銅"))
d=int(input("優"))
if a>fre:
    a=fre
if b>fre:
    b=fre
if c>fre:
    c=fre
if d>fre:
    d=fre
dict1["金"]=a
dict1["銀"]=b
dict1["銅"]=c
dict1["優"]=d
for key,value in dict1.items():
    print(key+"牌得到"+str(value)+"面")