num = list(map(int,input().split()))
k = int(input())
s = ''
for i in num:
    s+=str(i)
s = int(s)+k
num.clear()
a = list(str(s))
print(a)