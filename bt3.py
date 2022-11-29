def Function(a, b):
	a = int(a)
	b = int(b)
	if b == 0:
		return 1
	elif b%2 == 0:
		return Function(a, b/2)*Function(a, b/2)
	else:
		return Function(a, b/2)*Function(a, b/2)*a

print("nhap so a: ")
a = input()
print("nhap so b: ")
b = input()
print("Ket qua la: ", Function(a, b))				