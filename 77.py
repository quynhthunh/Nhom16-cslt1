a=str(int(input('so nhi phan:')))
res=0
i=0
while i<=len(str(a)):
    d=int(a)%10
    if len(str(a))!=0 and (d==0 or d==1):
        res=d*2**i+res
        i=i+1
        a=int(a)/10
print('so thap phan tuong ung la:',res,sep='')