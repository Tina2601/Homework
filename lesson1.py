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

# 2 possible with enter:
n1 = (input("Please, enter a number: "))
reversed = int(str(n1) [:: -1])
print(reversed)

# 3 possible one line :
n = int(input("enter a numder:  ") [:: -1])
print(n)
# 3 possible with word :
n = str(input("enter a word:  ") [:: -1])
print(n)


#EX 6: Квадрати натуральних чисел
n = int(input('Enter a number: '))
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1


#EX 7 : Рядок \ визначити кількість слів
sentence = input('')
word_count = sentence.count(' ')
print(word_count)

# possible 2 with split\ len - рахує пробіли !
sentence = input('')
word_count = sentence.split(' ')
print(len(word_count))
# one line : - рахує пробіли !
sentence = input('')
print(len(sentence.split(' ')))

#EX 8: Пошук символа у рядку
s = (input('Enter a sentence: '))
ch = (input('Enter a symbol: '))
if ch in s:
    print(s.find(ch), s.rfind(ch))