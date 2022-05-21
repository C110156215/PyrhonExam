total=[]
a=int(input("國文: "))
b=int(input("英文: "))
c=int(input("微積分: "))
d=int(input("體育: "))
e=int(input("程式設計: "))
dict1={a:"國文",b:"英文",c:"微積分",d:"體育",e:"程式設計"}
total.append(a)
total.append(b)
total.append(c)
total.append(d)
total.append(e)
total.sort()
max=total[4]
min=total[0]
print("平均分數: "+str((a+b+c+d+e)/len(total)))
print("最高分科目:"+str(dict1[max])+str(max)+"分")
print("最低分科目:"+str(dict1[min])+str(min)+"分")