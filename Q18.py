dict1={"A":1,"J":11,"Q":12,"K":13}
a=input("輸入: ")
b=a.split(" ")
sum=0
x=0
for i in range(5):
    if b[i]=="A" or b[i]=="J" or b[i]=="Q" or b[i]=="K":
        x=dict1[b[i]]
        sum+=int(x)
    else:    
        sum+=int(b[i])
print(sum)