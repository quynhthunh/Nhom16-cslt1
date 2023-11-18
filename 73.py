import string
chuoi = input("Nhap vao mot chuoi: ")
chuoi = chuoi.lower()
chuoi = chuoi.replace(" ", "")
chuoi = chuoi.translate(str.maketrans('', '', string.punctuation))
chuoi_dao_nguoc = chuoi[::-1]
if chuoi == chuoi_dao_nguoc:
    print("Chuoi nhap vao la mot palindrome.")
else:
    print("Chuoi nhap vao khong phai la mot palindrome.")