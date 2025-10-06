#Kiểm tra xem một số có phải là lũy thừa của 2 hay không. Sử dụng các toán tử bitwise để xác định xem một số có phải là lũy thừa của 2 hay không
n=int(input("Nhập một số nguyên dương: "))
if n>0 and (n & (n - 1)) == 0:
    print(n, "là lũy thừa của 2")
else:
    print(n, "không phải là lũy thừa của 2")