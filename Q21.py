dict1={"123":0,"456":1,"789":2,"321":3,"654":4}
total=[
    ["Tom","DTGD"],
    ["Cat","CSIE"],
    ["Nana","ASIE"],
    ["Lim","DBA"],
    ["Won","FDD"]
]
a=input("輸入查詢學號為: ")
if a in dict1:
    print("學生資料為: "+str(a)+" "+str(total[dict1[a]][0])+" "+str(total[dict1[a]][1]))
else:
    print("查無資料")