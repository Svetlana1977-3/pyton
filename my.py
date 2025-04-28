# print("Svetlana")
# a=2**5
# b=10
# print((a+b)*3-15)
# print("result" "=" "111")
# a = int(input("введите первое число: 4"))
# print(a)
# b = int(input("введите второе число: 1"))
# print("a =", a)
# print("b =", b)
# print("сумма a+b", a+b)
# # логический тип данных
# bool(0)
# bool(-1)
# bool(5)
# bool(0.0)
# bool(True)
# bool(False)
# bool("")
# bool(" ")
# print(bool("Привет мир!"))
print(2 == 2)
print(2 == "2")
print(4 < 2)
print(5 >= 5)
print(10 <= 5)
x = 5
a = 1
b = 10
print(a < x < b)
# строки (string)
print("строка в двойных кавычках")
print("строка в одинарных ковычках")
print("М.Ю. Лермонтов 'Бородино'")
print("М.Ю. Лермонтов \"Бородино\"")
# перенос строки
print("hfdysvj,hfpjv kjnrggrdfngkjf\n kdfgnkzdfjvjfdbn,jfbn"
      "fjbgr,jgblrkgjblkfjnbfkb"
      "dhvbljdrbvlkdjgbv,fdjbv,")
# Как объединить две строки в одну?
print("Можно " + "их " + "сложить")
print("5" + "5") #слияние (конкатенация)
print(5 + 5) # вычисление
print("5" *3) # дубликация
a = 5
b = 10
result = a + b
print(a, "+", b, "=", result)
final_v2 = (f"Результат выражения:\n"
f"{a} + {b} = {a+b}")
# списки (list)
myList = ["строка", 567, 78, True]
print(myList)
print(myList[0:3])
print(myList[1:])
# кортеж Tuples
myTuple = (78, 89.9, True, "Строка")
print(myTuple)
print(myTuple[0])
print(myTuple[3])
print(myTuple[2:4])
print(myTuple[1:])
# словари
myDict = {"name": "Svetlana", "Pole": "QA", 123: 456}
print(myDict["name"])
print(myDict["Pole"])
print(myDict[123])
name = "Svetlana"
myDict = {
      "name": name,
      "Pole": "QA"
}
# Множества (sets)
myList = [1, 2, 3, 3, 3, 4, 5]
mySet = set(myList)
print(mySet)
myList = ["Добрый", "добрый", "день", "день"]
mySet = set(myList)
print(mySet)
x = 5.67
x = int(x)
print(x)
x = str(x)
print(x+"строка")
x = float(x)
print(x)
a = "Привет мир!"
print(a[0])
a = list(a)
print(a)

myList = [1, 2, 3, 3, 3, 4, 5]
mySet = set(myList)
myList = list(mySet)
print(myList)
myTuple = tuple(myList)
print(myTuple)

print(ord("а"))
print(chr(1072))
print(f"\\{ord("а"):04x}")

# операторы
a = 5
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(7%2) #нечетное остаток есть
print(8%2) # четное, нет остатка
print(a**2)
print(10//3) # округление до целого первого числа
print(-10//3) # округление в большую сторону
print(5 == 5)
print(5 != 10)
print(5 > 10)

a += b
a -= b
a *= b
print(a)
a //= b
print(a)

# (5+10)*(3-2)+5^2