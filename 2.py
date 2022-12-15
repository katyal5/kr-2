a=str(input())
b=0
c=0
for i in range(len(a)):
    if ((a[i]!=' ') and (a[i]!=0) and (a[i]!='1') and (a[i]!='2') and (a[i]!='3') and (a[i]!='4') and (a[i]!='5') and (a[i]!='6') and (a[i]!='7') and (a[i]!='8') and (a[i]!='9')):
        b+=1
    else:
        if a[i]!=' ':
            c+=1
print('количество букв =',b,', количество цифр =',c)
