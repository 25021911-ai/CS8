#Nhập vào hai số nguyên a, b. Nếu cả hai số a, b đều âm thì in ra "Yes", ngược lại in ra "No".
a, b=map(int, input('Nhập hai số a,b: ').split())
if a<0 and b<0:
    print("Yes")
else:
    print("No")