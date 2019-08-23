
num = int(input())

ar  = list(map(int,input().rstrip().split()))



ar.sort()
ar.append('#')
print(ar)
def pairMerchant(ar,num):
    i = 0
    count = 0
    while i < num:
        if ar[i]==ar[i+1]:
            count = count + 1
            i = i + 2
        else:
            i = i+1
    return count


print(pairMerchant(ar,num))