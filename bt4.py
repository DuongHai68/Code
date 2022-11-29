y = int()
print("nhap so y: ")
y = input()
def mystery(x, n):
	global y
	x = int(x)
	n = int(n)
	if n == 0:
		return 1
	elif n%2 == 1:
		y = mystery(x, (n-1)/2)
		return x*y*y
	else:
		y = mystery(x, n/2)
		return y*y
print("nhap so x: ")
x = input()
print("nhap so n: ")
n = input()
print("ket qua la: ", mystery(x, n))
print("gia tri cua y trong ham la: ", y)