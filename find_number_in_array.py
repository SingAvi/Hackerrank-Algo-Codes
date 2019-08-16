



def birthday(s,d):
    day = 0
    month = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] + s[j] == d:
                day = day + 1

    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] + s[j] == m:
                month = month + 1
    qq = day , month
    return qq



s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = dm[0]
m = dm[1]

result = birthday(s,d)
print(result)