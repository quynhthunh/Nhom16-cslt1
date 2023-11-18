import random
s=0
for i in range(10):
    flips=0
    H=0
    T=0
    while True:
        kq=random.choice(['H','T'])
        print(kq,end=' ')
        flips=flips+1
        if kq=='H':
            H=H+1
            T=0
        elif kq=='T':
            T=T+1
            H=0
        if H==3 or T==3:
            break
    print('(',flips,'flips',')',sep=' ')
    s=s+flips
tb=s/10
print('On average,',tb,'flips were needed')
