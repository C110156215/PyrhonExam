a=int(input("輸入一正整數: "))
ans=""
if 11<=a<=1000:
    if a%2==0 and a%11==0 and a%5!=0 and a%7!=0:
        ans="Yes"
    else:
        ans="No"
    print(str(a)+"為新公倍數?: "+str(ans))
else:
    print("輸入錯誤")