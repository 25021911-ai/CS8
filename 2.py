#Hoán đổi hai số không sd biến tạm thời
#Sử dụng phép toán XOR bitwise để hoán đổi giá trị của hai biến.
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print("Trước khi hoán đổi: a =", a, ", b =", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("Sau khi hoán đổi: a =", a, ", b =", b)