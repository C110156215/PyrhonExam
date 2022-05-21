M=int(input("請輸入階乘值M: "))
N=1
total=1
while total<M:
    total=total*N
    N=N+1
print("超過 M 為"+str(M)+"的最小階層 N 值為 :"+str(N-1))