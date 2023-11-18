# cách 1:
chuoi = input("Nhap vao mot chuoi: ")
chuoi_dao_nguoc = chuoi[::-1]
if chuoi == chuoi_dao_nguoc:
    print(chuoi, "la mot palindrome.")
else:
    print(chuoi, "khong la mot palindrome.")

# cách 2:
chuoi=input("Nhap vao mot chuoi: ")
palindrome=True
for i in range(len(chuoi)//2):
    if chuoi[i]!=chuoi[len(chuoi)-i-1]:
        palindrome=False
if palindrome:
    print(chuoi,"la mot palindrome.")
else:
    print(chuoi,"khong la mot palindrome.")