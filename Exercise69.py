pi = 3
sign = 1
MauSo = 2
for i in range(1, 16):
    pi = pi + sign * 4 / (MauSo * (MauSo + 1) * (MauSo + 2))
    sign = sign * -1
    MauSo = MauSo + 2
    print("Phep tinh gan dung ",i,": ",pi,sep="")
