def pow(n):
	n = int (n)
	if n == 0:
		return 1
	else:
		return pow(n-1) + pow(n-1)
print("nhap so n: ")
n = input()
print("ket qua la: ", pow(n))