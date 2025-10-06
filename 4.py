#viêt chương trình chia một số m cho n, kết quả thu được làm tròn xuống
m, n=map(int, input("m,n là:").split())
a=m/n
import math
print("Kết quả làm tròn xuống là:", math.floor(a))