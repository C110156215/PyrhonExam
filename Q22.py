
dict1={"123":0,"456":1,"789":2,"336":3,"775":4,"566":5}
total=[
    ["456","9000"],
    ["789","5000"],
    ["888","6000"],
    ["558","10000"],
    ["666","12000"],
    ["221","7000"]
]
a=int(input("輸入查詢組數N為: "))
while a!=0:
    b=input("輸入: ")
    c=b.split(" ")
    if b[0] in dict1:
        if c[1]==total[dict1[c[0]]][0]:
            print(total[dict1[c[0]]][1])
        else:
            print("error")
    else:
        print("error")

    a-=1