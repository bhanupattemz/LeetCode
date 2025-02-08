data=[[3,4],[2,3],[2,2]] 
result=[]
for item in data:
    if(item[0]>len(result)):
        [result.append(False) for j in range(len(result),item[0]-1)]
    for i in range(item[0]-1,item[1]):
        if(i<len(result)):
            result[i]= not result[i]
        else:
            result.append(True)
sum=0
for i in range(len(result)):
    sum+=(i+1) if result[i] else 0
print(f"Result:{result}\nSum:{sum}")