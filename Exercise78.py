q=int(input('so thap phan:'))
kq=str('')
r=int()
while q>0:
    r=q%2
    kq=str(r)+kq
    q=q//2
    if q==0:
        break
print('so nhi phan tuong ung la:',kq)
