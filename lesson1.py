n = int(input("How many students?  :"))
k = int(input("How many apples?  :"))
print(int(k) // (n))
print(int(k) % (n))


a = int(input("How many students are in total?:  "))
b = int((a) / 3)
c = int((b) / 2)
d = int((c) * 3)
print(int(b),(c),(d))
# or open answer:
print("Nun of students in every class:" + str(b), "Desks in every class:" + str(c), "Desks for all 3 classes:" + str(d))
# question: why the class 'int' was saved? -
print((a), type(a))



n1 = 123
reversed = int(str(n1)[:: -1])
print(reversed)

n2 = 867
reversed = int(str(n2)[:: -1])
print(reversed)

n3 = 374
reversed = int(str(n3)[:: -1])
print(reversed)

