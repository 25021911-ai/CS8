#Nhập vào một số nguyên dương x, bạn hãy kiểm tra xem x là số chẵn hay lẻ. Nếu x là số chẵn, in ra "Even". Nếu x là số lẻ, in ra  "Odd". 
x=int(input("Nhập một số nguyên dương x: "))
if x>0 and x%2==0:
    print(x, "Even")
elif x>0:
    print(x, "Odd")
else:
    print("Số không hợp lệ")