s=0
print("Nhap gia tien cua hang hoa: ")
while True:
    i=input()
    if i=="":
        break
    i=float(i)
    s=s+i
print("Tong chi phi la: ",s)
if s %5 < 2.5:
    t=(s//5)*5
elif s%5 > 2.5:
    t=(s//5 +1)*5
print("So tien phai tra bang tien mat la: ",t)
