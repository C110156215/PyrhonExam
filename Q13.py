word = input("輸入一字元為: ")
if str(word) == "".join(reversed(word)) :
    print("YES")
else:
    print("NO")