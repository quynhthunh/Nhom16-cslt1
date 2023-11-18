s=0.00
while True:
    n=input("Nhap tuoi cua khach: ")
    if n=="":
        break
    n=int(n)
    if n<=2:
        t=0.00
    elif 3<=n<=12:
        t=14.00
    elif n>=65:
        t=18.00
    elif 13<=n<=64:
        t=23.00
    s=s+t
print("Chi phi ve vao cong la: ",s)
