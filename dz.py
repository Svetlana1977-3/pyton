print("Светлана")

#20.04.2025
a=2**5
b=10
print((a+b)*3-15)
print("result" "=" "111")

#26.04.2025
name = "Светлана", "47", "Да"
print(name)

y = 3
x = 5
print(y > x - 2)

#27.04.2025
myList = ["Светлана", "47", "Да"]
mySet = set(myList)
myList = list(mySet)
print(myList)

#11/05/2025
x = float(input("введите число: "))
if -9 < x < 2:
    print("число находится в интервале (-9; 2)")
else:
    print("число НЕ находится в интервале (-9; 2)")

#11.05.2025 ДЗ
#Задание 7
a = int(input("Вести первое число: "))
b = int(input("Вести второе чтсло: "))
c = int(input("Вести третье число: "))
nums = [a, b, c]
nums.sort()
print("Ввести число в порядке возрастания", nums[0], nums[1], nums[2])

#Задание 8

# Введите продажи менеджеров
sales1 = float(input("Вести уровень продаж менеджера 1: "))
sales2 = float(input("Вести уровень продаж менеджера 2: "))
sales3 = float(input("Вести уровень продаж менеджера 3: "))

a = 200

if a <= 500:
    commission = a * 0.03
elif a <= 1000:
    commission = a * 0.05
else:
    commission = a * 0.08
    total_salary = a + commission
print("total_salary")

# Расчет зарплаты

#Расчёт ЗП первого менеджера
if sales1 <= 500:
     salary1 = 200 + sales1 * 0.03
elif sales1 <= 1000:
     salary1 = 200 + sales1 * 0.05
else:
     salary1 = 200 + sales1 * 0.08

#Расчёт ЗП второго менеджера
if sales2 <= 500:
    salary2 = 200 + sales2 * 0.03
elif sales2 <= 1000:
    salary2 = 200 + sales2 * 0.05
else:
    salary2 = 200 + sales2 * 0.08
#Расчёт ЗП третьего менеджера
if sales3 <= 500:
    salary3 = 200 + sales3 * 0.03
elif sales3 <= 1000:
    salary3 = 200 + sales3 * 0.05
else:
    salary3 = 200 + sales3 * 0.08
# # Определяем лучшего менеджера
best_salary = max(salary1, salary2, salary3)

if best_salary == salary1:
    salary1 += 200
    best = 1
elif best_salary == salary2:
    salary2 += 200
    best = 2
else:
    salary3 += 200
    best = 3
print(f"Зарплата 1 менеджера: {salary1}")
print(f"Зарплата 2 менеджера: {salary2}")
print(f"Зарплата 3 менеджера: {salary3}")
print(f"Лучший менеджер: {best}-ий")

# Задание 9

year = int(input("Введите год: "))
month = int(input("Введите номер месяца (1-12): "))
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
     print("29 дней")
    else:
     print("28 дней")
elif month in [1, 3, 5, 7, 8, 10, 12]:
     print("31 день")
elif month in [4, 6, 9, 11]:
     print("30 дней")
else:
     print("Некорректный номер месяца")

#Задание 10

age = int(input("Введите возраст: "))
time = int(input("Введите время сеанса (в часах, например 14): "))
price = 0

if age < 3:
    price = 0
elif age <= 12:
    price = 10
else:
    price = 15
if time <= 12 and price > 0:
    price *= 0.8
print(f"Стоимость билета к оплате: {price}")
