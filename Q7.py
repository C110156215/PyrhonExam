a=input("輸入月租費型式及通話時間為:")
end=a.split(",")
enddol=0

if int(end[0])==186:
    dol=int(end[1])*0.09
    if dol<186:
        enddol=186
    elif 372>=dol>186:
        enddol=dol*0.9
    else:
        enddol=dol*0.8

elif int(end[0])==386:
    dol=int(end[1])*0.08
    if dol<386:
        enddol=386
    elif 772>=dol>386:
        enddol=dol*0.8
    else:
        enddol=dol*0.7

elif int(end[0])==586:
    dol=int(end[1])*0.07
    if dol<586:
        enddol=586
    elif 1172>=dol>586:
        enddol=dol*0.7
    else:
        enddol=dol*0.6

elif int(end[0])==986:
    dol=int(end[1])*0.06
    if dol<986:
        enddol=386
    elif 1572>=dol>986:
        enddol=dol*0.6
    else:
        enddol=dol*0.5

print(round(enddol))