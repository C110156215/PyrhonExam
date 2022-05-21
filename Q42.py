a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
func=(b**2)-(4*a*c)
ans=0
ans1=0
if func>0:
    ans=(((-1)*b)+(func)**0.5)/2*a
    ans1=(((-1)*b)-(func)**0.5)/2*a
    print(round(ans))
    print(round(ans1))
elif func<0:
    ans=0
    print(round(ans))
elif func==0:
    ans=(-1*b)/2*a
    print(round(ans))