d=0
p=0
import math
while True:
    x=input("x= ")
    if x=="":
        print("chu vi da giac la: ",p)
        break
    y=input("y= ")
    x=float(x)
    y=float(y)
    d=d+1
    p=p+2
    if d>2:
        p=(p/2-1) + math.sqrt((x-x1)**2+(y-y1)**2)
        x1=x
        y1=y
    else:
        x1=x
        y1=y