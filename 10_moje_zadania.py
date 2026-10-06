# Zadanie 1
# Wyświetl:
# - pierwszy element,
# - ostatni element,
# - trzeci element,
# - pierwsze 3 elementy,
# - wszystkie elementy od indeksu 2 do końca.

# numbers = [4, 8, 15, 16, 23, 42]
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])
# print(numbers[:3])
# print(numbers[2:])

# Zadanie 2 Dodaj "Karolina" na koniec listy.
# names = ["Ania", "Kasia", "Piotr"]
# names.append("Karolina")
# print(names)

# Zadanie 3 Dodaj "Kasia" tak, żeby znalazła się pomiędzy "Ania" i "Piotr".

# names = ["Ania", "Piotr", "Karolina"]
# names.insert(1, "Kasia")
# print(names)

# Zadanie 4 Usuń z listy wartość 30.

# numbers = [10, 20, 30, 40, 50]
# numbers.remove(30)
# print(numbers)


# Zadanie 4 Usuń pierwsze wystąpienie "banana" za pomocą remove() i wyświetl listę
# fruits = ["apple", "banana", "orange", "banana"]
# fruits.remove("banana")
# print(fruits)

# Zadanie 5 Usuń ostatni element za pomocą pop() i zapisz usuniętą wartość do zmiennej: deleted_number

# numbers = [10, 20, 30, 40, 50]
# deleted_number = numbers.pop()
# print(deleted_number)

# Zadanie 6 Sprawdź, czy "Karolina" znajduje się na liście.
# users = ["Ania", "Piotr", "Karolina", "Maciej"]

# if "Karolina" in users:
#     print("Użytkownik istnieje")

# Zadanie 7 Posortuj oryginalną listę rosnąco i ją wyświetl.
# numbers = [8, 2, 10, 1, 5]
# numbers.sort()
# print(numbers)


# Zadanie 8 Utwórz nową listę sorted_numbers, która będzie posortowana rosnąco, ale nie zmieniaj numbers. Na końcu wyświetl obie listy.
# numbers = [8, 2, 10, 1, 5]

# sorted_numbers=sorted(numbers)
# print(numbers, sorted_numbers)

# Zadanie 9 Odwróć kolejność elementów bez sortowania
# numbers = [10, 20, 30, 40]

# numbers.reverse()
# print(numbers)

# Zadanie 10 Stwórz za pomocą range() liczby:
# 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
# a potem zamień wynik na listę i ją wyświetl.

# numbers = list(range(0,20,2))
# print(numbers)


# Zadanie 11 Stwórz pustą listę. Następnie za pomocą for dodaj do niej kwadraty wszystkich liczb z numbers.
# numbers = [2, 4, 6, 8]
# squared_numbers = []

# for number in numbers:
#     squared_numbers.append(number**2)

# print(squared_numbers)

# Zadanie 12 Dodaj do big_numbers tylko liczby większe niż 7.
# numbers = [1, 5, 8, 12, 3, 20]
# big_numbers = []

# for number in numbers:
#     if number>7:
#         big_numbers.append(number)

# print(big_numbers)

# Zadanie 13 Wyświetl wartość znajdującą się pod kluczem "name" używając metody .get().
# user = {
#     "name": "Karolina",
#     "age": 33,
#     "city": "Wroclaw"
# }

# print(user.get("name"))
# user['job']='Frontend Developer'
# user['age']=34
# print(user)
# user.pop("city")
# print(user)

# for key in user.keys():
#     print(key)

# for value in user.values():
#     print(value)

# for key,value in user.items():
#     print(f"{key}:{value}")

# Zadanie 14 Za pomocą pętli zbuduj słownik:
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = {}

# for number in numbers:
#     squared_numbers[number]=number**2

# print(squared_numbers)


# Zadanie 15 Masz 2 listy. Zbuduj słownik:  {
#     "Ania": 28,
#     "Piotr": 35,
#     "Karolina": 33
# }
# names = ["Ania", "Piotr", "Karolina"]
# ages = [28, 35, 33]
# dane = {}

# for i in range(len(names)):
#     dane[names[i]]=ages[i]

# print(dane)


# products = ["apple", "banana", "orange"]
# prices = [4, 7, 6]
# amount = {}

# for i in range(len(products)):
#     amount[products[i]]=prices[i]

# print(amount)

# Zadanie 16 Dodaj do listy imiona tylko tych osób, które mają więcej niż 30 lat.
# users = {
#     "Ania": 28,
#     "Piotr": 35,
#     "Karolina": 33,
#     "Maciej": 25
# }

# older_users = []

# for key,value in users.items():
#     if value>30:
#         older_users.append(key)

# print(older_users)


# Zadanie 17  Dodaj do słownika tylko te produkty, których cena jest większa niż 5.
# products = {
#     "apple": 4,
#     "banana": 7,
#     "orange": 6,
#     "pear": 3
# }

# expensive_products = {}

# for key,value in products.items():
#     if value>5:
#         expensive_products[key]=value

# print(expensive_products)

# Zadanie 18  Zwiększ cenę każdego produktu o 2.
# products = {
#     "apple": 4,
#     "banana": 7,
#     "orange": 6
# }

# for key,value in products.items():
#     products[key] = value+2

# print(products)

# Zwiększ wynik każdej osoby o 5 i wyświetl zmodyfikowany słownik.
# scores = {
#     "Ania": 10,
#     "Piotr": 7,
#     "Karolina": 12
# }

# for key, value in scores.items():
#     scores[key]=value+5

# print(scores)

# Zadanie 19 Usuń ze słownika wszystkie osoby, które mają mniej niż 30 lat.

# users = {
#     "Ania": 28,
#     "Piotr": 35,
#     "Karolina": 33,
#     "Maciej": 25
# }

# for key, value in users.items():
#     if value<30:
#         del key

# print(users)

# Zadanie Funkcja ma znaleźć tylko użytkowników z "active": True, pominąć osoby poniżej 30 lat, stworzyć i zwrócić słownik w postaci: {"Karolina": 33 }

# users = [
#     {"name": "Ania", "age": 28, "active": True},
#     {"name": "Piotr", "age": 35, "active": False},
#     {"name": "Karolina", "age": 33, "active": True},
#     {"name": "Maciej", "age": 25, "active": True},
#     {"name": "Ola", "age": 41, "active": False}
# ]


# def get_active_users(users):

#     chosen_users = {}

#     for user in users:
#         if user['age'] >= 30 and user['active']:
#             chosen_users[user["name"]] = user['age']

#     return chosen_users


# result = get_active_users(users)
# print (result)

# Zadanie
# products = [
#     {"name": "Laptop", "price": 4500, "available": True},
#     {"name": "Mouse", "price": 120, "available": False},
#     {"name": "Keyboard", "price": 350, "available": True},
#     {"name": "Monitor", "price": 1200, "available": True},
#     {"name": "Headphones", "price": 500, "available": False}
# ]

# def get_available_expensive_products(products):

#     chosen_products = {}

#     for product in products:
#         if product["available"] and product["price"] > 500:
#             chosen_products[product["name"]] = product["price"]

#     return chosen_products

# result = get_available_expensive_products(products)
# print(result)

# Zadanie Napisz funkcję, która zwróci sumę opłaconych zamówień dla każdego użytkownika:
# {
#     "Ania": 320,
#     "Karolina": 300,
#     "Piotr": 150
# }

# orders = [
#     {"user": "Ania", "amount": 120, "paid": True},
#     {"user": "Piotr", "amount": 80, "paid": False},
#     {"user": "Ania", "amount": 200, "paid": True},
#     {"user": "Karolina", "amount": 300, "paid": True},
#     {"user": "Piotr", "amount": 150, "paid": True},
#     {"user": "Karolina", "amount": 50, "paid": False},
# ]


# def get_amount_of_paid_orders(orders):

#     sum = {}

#     for order in orders:
#         if order["paid"]:
#             if order["user"] in sum:
#                 sum[order["user"]] += order["amount"]

#             else:
#                 sum[order["user"]] = order["amount"]

#     return sum


# result = get_amount_of_paid_orders(orders)
# print(result)


# Zadanie Napisz funkcje która znajdzie najdroższy produkt i zwróci cały jego słownik.

# products = [
#     {"name": "Laptop", "price": 4500, "category": "electronics"},
#     {"name": "Mouse", "price": 120, "category": "electronics"},
#     {"name": "Desk", "price": 900, "category": "furniture"},
#     {"name": "Chair", "price": 700, "category": "furniture"},
#     {"name": "Monitor", "price": 1500, "category": "electronics"}
# ]

# def get_most_expensive_product(products):

#     most_expensive_product={}
#     biggest_price=0

#     for product in products:
#         if product["price"]>biggest_price:
#             biggest_price = product["price"]
#             most_expensive_product=product

#     return most_expensive_product

# result=get_most_expensive_product(products)
# print(result)


# Zadanie Napisz funkcję, która zwróci listę imion osób mających podany skill.

users = [
    {"name": "Ania", "skills": ["Python", "SQL"]},
    {"name": "Piotr", "skills": ["JavaScript", "React"]},
    {"name": "Karolina", "skills": ["Python", "React", "JavaScript"]},
    {"name": "Maciej", "skills": ["Java", "SQL"]}
]


def find_users_with_skill(users, skill):

    skilled_users = []

    for user in users:
        if skill in user["skills"]:
            skilled_users.append(user["name"])

    return skilled_users

result = find_users_with_skill(users, "React")
print(result)
