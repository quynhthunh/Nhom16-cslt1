n=int(input('Enter an integer:'))
i=2
if n<2:
    print('loi,vui long nhap lai so lon hon hoac bang 2')
print('The prime factors of',n,'are:')
while i<=n:
    if n%i==0:
        print(i)
        n=n//i
    elif n%i != 0:
        i=i+1
