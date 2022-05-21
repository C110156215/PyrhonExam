a=input("請輸入英文句子: ")
b=a.split(" ")
ans=[]
for i in range(7,-1,-1):
    ans.append(b[i])
print("輸出結果: ")
print(ans)