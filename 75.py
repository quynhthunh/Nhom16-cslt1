m=int(input('m='))
n=int(input('n='))
d=min(m,n)
while True:
    if m%d != 0 or n%d != 0:
        d=d-1
    else:
        print('uoc chung lon nhat giua',m,'va',n,'la:',d)
        break