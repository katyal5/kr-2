a=list(map(int,input().split()))
b=[]
c=99999999999999
for i in range(len(a)):
    if a[i]<0:
        b.append(-a[i])
    else:
        b.append(a[i])
print(b)
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if abs(b[i]-b[j])<c:
            c=abs(b[i]-b[j])
print(c)
