dict1={}
n=int(input("輸入筆數n(>=4筆): "))
if n>=4:
    for i in range(n):
        a=input("輸入: ")
        b=a.split(" ")
        dict1[b[0]]=b[1]
    find=input("輸入欲查詢單字: ")
    if find in dict1:
        print(str(find)+"中文意思為"+str(dict1[find]))
    else:
        print("字典未有此單字")
else:
    print("筆數錯誤")