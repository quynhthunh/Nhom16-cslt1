import random
max=0
dem=0
for i in range(1,100):
    n=random.randint(1,100)
    if n>max:
        max=n
        print(n,'<== Update')
        dem=dem+1
    elif n==max:
        print(n,"<== Update")
    else:
        print(n)
print('gia tri toi da gap phai la',max)
print('so lan gia tri toi da duoc cap nhap trong qua trinh nay la',dem,'lan')
