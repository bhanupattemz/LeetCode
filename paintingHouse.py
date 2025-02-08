n,s0,k,b,m,a=3,1,1,1,2,4
data=[s0]
num=0
for i in range(1,n+1):
    s=((k*data[i-1]+b)%m)+1+data[i-1]
    data.append(s)
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{data[i]},{data[j]}")
        if data[i]*data[j]<=a:
            num+=1
print(f"S:{data}\ncombinations:{n}")