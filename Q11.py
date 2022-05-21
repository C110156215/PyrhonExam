dict1={"水瓶":"Aquarius","雙魚":"Pisces","牡羊":"Aries","金牛":"Taurus","雙子":"Gemini","巨蟹":"Cancer","獅子":"Leo","處女":"Virgo","天秤":"Libra","天蠍":"Scorpio","射手":"Sagittarius","魔羯":"Capricorn",}
date=input("輸入月及日為: ")
end=date.split(" ")
m=int(end[0])
d=int(end[1])

if m==1:
    if d<=20:
        print("星座為: "+dict1["魔羯"])
    else:
        print("星座為: "+dict1['水瓶'])

elif m==2:
    if d<=18:
        print("星座為: "+dict1["水瓶"])
    else:
        print("星座為: "+dict1['雙魚'])

elif m==3:
    if d<=20:
        print("星座為: "+dict1["雙魚"])
    else:
        print("星座為: "+dict1['牡羊'])

elif m==4:
    if d<=20:
        print("星座為: "+dict1["牡羊"])
    else:
        print("星座為: "+dict1['金牛'])

elif m==5:
    if d<=21:
        print("星座為: "+dict1["金牛"])
    else:
        print("星座為: "+dict1['雙子'])

elif m==6:
    if d<=21:
        print("星座為: "+dict1["雙子"])
    else:
        print("星座為: "+dict1['巨蟹'])

elif m==7:
    if d<=22:
        print("星座為: "+dict1["巨蟹"])
    else:
        print("星座為: "+dict1['獅子'])

elif m==8:
    if d<=23:
        print("星座為: "+dict1["獅子"])
    else:
        print("星座為: "+dict1['處女'])

elif m==9:
    if d<=23:
        print("星座為: "+dict1["處女"])
    else:
        print("星座為: "+dict1['天秤'])

elif m==10:
    if d<=23:
        print("星座為: "+dict1["天秤"])
    else:
        print("星座為: "+dict1['天蠍'])

elif m==11:
    if d<=22:
        print("星座為: "+dict1["天蠍"])
    else:
        print("星座為: "+dict1['射手'])

elif m==12:
    if d<=21:
        print("星座為: "+dict1["射手"])
    else:
        print("星座為: "+dict1['魔羯'])