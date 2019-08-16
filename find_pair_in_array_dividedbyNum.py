arr = list(map(int,input().rstrip().split()))
k = 3
count = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        summ = arr[i]+arr[j]
        if summ%k==0:
            count = count+1
            print(arr[i],arr[j])
print(count)

