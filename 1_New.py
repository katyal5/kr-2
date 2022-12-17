a=list(map(int,input().split()))
b=[]
c=99999999999999
for i in range(len(a)):
    if a[i]<0:
        b.append(-a[i])
    else:
        b.append(a[i])
raz=abs(a[1]-a[2])
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if raz>abs(a[i-1]-a[j-1]):
            z=i-1; x=j-1;
print(b[z], b[x])
