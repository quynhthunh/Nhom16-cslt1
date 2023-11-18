i=float(input("Nhap gia tri: "))
s=0
if i==0:
    print("Loi, vui long nhap lai gia tri khac")
else:
    s=s+i
    d=0
    while True:
        i=float(input("Nhap gia tri: "))
        s=s+i
        d=d+1
        if i==0:
            print("Gia tri trung binh la:",s/d)
            break
