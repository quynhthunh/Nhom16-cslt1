while True:
    chuoi=input("Nhap mot chuoi 8 bit: ")
    if chuoi=="":
        break
    if len(chuoi)!=8:
        print("Loi. Yeu cau nhap lai chuoi 8 bit.")
        continue
    ones=chuoi.count("1")
    if ones%2==0:
        print("Parity bit cua chuoi la 0.")
    else:
        print("Parity bit cua chuoi la 1.")