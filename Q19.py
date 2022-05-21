ro=int(input("測試的資料量: "))

while ro!=0:
    ro-=1
    a=input("輸入血型: ")
    b=a.split(" ")
    fa=b[0]
    ma=b[1]
    c=b[2]

    if c=="O" or c=="A" or c=="B" or c=="AB":
        if fa=="O" and ma =="O":
            if c=="A" or c=="B" or c=="AB":
                print("IMPOSSIBLE")
            else: 
                print("YES")

        elif fa=="O" and ma =="A":
            if c=="B" or c=="AB":
                print("IMPOSSIBLE")
            else: 
                print("YES")

        elif fa=="O" and ma =="B":
            if c=="A" or c=="AB":
                print("IMPOSSIBLE")
            else: 
                print("YES")

        elif fa=="O" and ma =="AB":
            if c=="O" or c=="AB":
                print("IMPOSSIBLE")
            else: 
                print("YES")

        elif fa=="A" and ma =="A":
            if c=="B" or c=="AB":
                print("IMPOSSIBLE")
            else: 
                print("YES")

        elif fa=="A" and ma =="B":
            print("YES")

        elif fa=="A" and ma =="AB":
            if c=="O":
                print("IMPOSSIBLE")
            else: 
                print("YES")

        elif fa=="B" and ma =="B":
            if c=="A" or c=="AB":
                print("IMPOSSIBLE")
            else: 
                print("YES")

        elif fa=="B" and ma =="AB":
            if c=="O":
                print("IMPOSSIBLE")
            else: 
                print("YES")

        elif fa=="AB" and ma =="AB":
            if c=="O":
                print("IMPOSSIBLE")
            else: 
                print("YES")
        else:
            print("輸入錯誤")
    else:
        print("輸入錯誤")
