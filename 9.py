#Nhập vào 3 số nguyên dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài cạnh của 1 tam giác được không. Nếu a, b, c cấu tạo thành được một tam giác, in ra "Yes". Ngược lại in ra "No"
a,b,c = map(int, input("Nhập độ dài ba cạnh tam giác: ").split())
if a+b>c and a+c>b and b+c>a:
    print("Yes")
else:
    print("No")