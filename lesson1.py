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


# 1 possible :
n1 = 123
reversed = int(str(n1)[:: -1])
print(reversed)

n2 = 867
reversed = int(str(n2)[:: -1])
print(reversed)

n3 = 374
reversed = int(str(n3)[:: -1])
print(reversed)

# 2 possible :
n1 = (input("Please, enter a number: "))
reversed = int(str(n1) [:: -1])
print(reversed)

# 3 possible :
n = int(input("enter a numder:  ") [:: -1])
print(n)
# 3 possible with word :
n = str(input("enter a word:  ") [:: -1])
print(n)

#EX 6:
a = [1, 4, 9, 16, 25, 36, 49]
n = 50
if n <= 50:
    n = a.sort()
print(a)

a = [1, 4, 9]
n = 10
if n <= 10:
    n = a.sort()
print(a)

a = [1, 4, 9]
n = 9
if n <= 9:
    n = a.sort()
print(a)

a = [1, 4]
n = 4
if n <= 4:
    n = a.sort()
print(a)

a = [1]
n = 1
if n <= 1:
    n = a.sort()
print(a)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n = 100
if n <= 100:
    n = a.sort()
print(a)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81]
n = 99
if n <= 99:
    n = a.sort()
print(a)