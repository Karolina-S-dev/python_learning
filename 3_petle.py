# while - nie wiemy ile razy, ale wiemy do kiedy
# for - iteracja lub wiemy ile razy
# break - przerwanie petli
# continue - przerwanie iteracji
# number = 1
# while number % 2 != 0:
#     number = float(input('Podaj liczbe parzystą: '))

# print('Gratulacje')

# print('Zakończono program')

# name = 'Karolina'

# for letter in name:
#     print(letter)
# print(letter) #a - ostatnia nadpisana wartosc

# print(len(name))

# for number in range(100, 201, 2):#<0;10)
#     #if number % 2 == 0:
#         print(number)


# ------------- ZADANIA DOMOWE --------------

# 5. Napisz program, który pobiera od użytkownika długość boków trójkąta i wyświetla informację, jaki to trójkąt. Program powinien zawierać blok warunkowy, który sprawdza, czy trójkąt jest równoboczny, równoramienny, czy różnoboczny i wyświetla odpowiedni komunikat.

# a=float(input('Podaj długość pierwszego boku trójkąta: '))
# b=float(input('Podaj długość drugiego boku trójkąta: '))
# c=float(input('Podaj długość drugiego boku trójkąta: '))

# if a==b and b==c:
#     print('Trójkąt jest równoboczny')
# elif a==b or b==c or a==c:
#     print('Trójkąt jest równoramienny')
# else:
#     print('Trójkąt jest różnoboczny')


# 4.Napisz program, który pobiera od użytkownika trzy liczby i wyświetla informację, która z nich jest największa. Program powinien zawierać blok warunkowy, który porównuje te liczby i wyświetla odpowiedni komunikat, np. liczba 123 jest większa od liczb 3 i 65.

# print('Sprawdzamy, która liczba jest największa')
# d = int(input('Podaj pierwszą liczbę całkowitą: '))
# e = int(input('Podaj pierwszą liczbę całkowitą: '))
# f = int(input('Podaj pierwszą liczbę całkowitą: '))

# if d > e and d > f:
#     print(f"Liczba {d} jest większa od {e} i {f}")
# elif e > d and e > f:
#     print(f"Liczba {e} jest większa od {d} i {f}")
# elif f > d and f > e:
#     print(f"Liczba {f} jest większa od {d} i {e}")
# else:
#     print(f"Liczby są równe")


# 3. Napisz program, który pobierze od użytkownika dwie liczby całkowite - początek i koniec przedziału. Następnie program ma wyświetlić wszystkie liczby parzyste z tego przedziału. W przypadku, gdy użytkownik poda błędne dane (np. początek większy niż koniec), program powinien wyświetlić stosowny komunikat o błędzie i poprosić o ponowne wprowadzenie danych.

# while True:
#     poczatek = int(input('Podaj liczbę całkowitą - początek przedziału: '))
#     koniec = int(input('Podaj liczbę całkowitą - koniec przedziału: ')) + 1

#     if poczatek > koniec:
#         print(
#             'Początek przedziału nie może być większy niż koniec. Wprowadź liczby ponownie.')
#         continue

#     else:
#         for number in range(poczatek, koniec):
#             if number % 2 == 0:
#                 print(number)

#     #operacje po petli
#     break

# tutaj miałam kłopot w ktorym miejscu ma byc break


# 2. Napisz program, który pobiera od użytkownika liczby, do momentu, aż użytkownik wybierze, że chce przestać. Program następnie powinien wypisać:
# srednia arytmetyczna
# najwieksza liczbe
# najmniejsza liczbe

# print('Witaj! Wpisz stop, aby zakończyć.')
# suma = 0
# licznik = 0

# while True:
#     liczba = input('Podaj liczbę całkowitą: ')

#     if liczba == 'stop':
#         break

#     liczba = int(liczba)

#     if licznik == 0:
#         max = liczba
#         min = liczba

#     suma += liczba
#     licznik += 1

#     if liczba > max:
#         max = liczba

#     if liczba < min:
#         min = liczba

# print(f"Średnia: {suma/licznik}")
# print(f"Największa: {max}")
# print(f"Najmniejsza: {min}")


# 1.Napisz program, który będzie symulował grę w ruletkę. Program powinien pozwalać użytkownikowi obstawiać liczby od 1 do 36 oraz kolor czerwony lub czarny. Po obstawieniu program powinien losować wynik ruletki i wyświetlać informację, czy gracz wygrał, czy przegrał oraz ile wygrał lub stracił pieniędzy.
# Program powinien mieć następujące funkcjonalności:
# Prosić użytkownika o obstawienie liczby lub koloru.
# Sprawdzać poprawność obstawienia (czy użytkownik podał poprawną liczbę lub kolor).
# Pytać użytkownika o wysokość stawki.
# Losować wynik ruletki (liczbę od 1 do 36 oraz kolor czerwony lub czarny).
# Sprawdzać, czy użytkownik wygrał lub przegrał.
# Informować użytkownika o wyniku gry oraz o wysokości wygranej lub straconej stawki.
# Pytać użytkownika, czy chce zagrać ponownie.

import random

balance = float(input('Ile masz kasy? '))  # saldo
print(f"Saldo: {balance} zł")

while True:

    # za ile PLN gracz chce zagrać
    user_money = int(input('Ile pieniędzy stawiasz (10-5000 zł)? '))
    if user_money > 5000 or user_money < 10 or user_money > balance:
        print('Podałeś nieprawidłową wartość')
        continue
    print(f"Grasz za {user_money} zł")

    # balance = balance - user_money;
    balance -= user_money
    print(f"Saldo: {balance} zł")

  # pytamy czy gracz chce obstawić kolor czy liczbę
    user_question = input("Chcesz obstawić liczbę czy kolor? (l/k): ")
    if user_question == "l":

        # obstawienie liczby przez gracza
        while True:
            user_number = input('Podaj liczbę od 1 do 36: ')
            if user_number == "":
                print('Nie podałeś liczby')
                continue
            int_user_number = int(user_number)
            if int_user_number >= 1 and int_user_number <= 36:
                print(f"Obstawiłes liczbę: {user_number}")

                # losowanie liczby
                draw_result = random.randint(1, 36)
                print(f"Wylosowana liczba to: {draw_result}")

                # Sprawdzenie, czy użytkownik wygrał czy przegrał
                if int_user_number == draw_result:
                    print(f"Wygrałes liczbę! 🎉 i {36 * user_money} zł")
                    balance += 36 * user_money
                else:
                    print("Przegrałes 😔")

                break
            else:
                print('podałeś niepoprawną wartość')

    # obstawienie koloru przez gracza
    elif user_question == "k":
        while True:
            user_colour = input('wybierz kolor: czerwony czy czarny? ').lower()

            if user_colour == 'czerwony' or user_colour == 'czarny':
                print(f"Obstawiłes kolor: {user_colour}")

                # losowanie koloru
                colours_result = random.choice(['czerwony', 'czarny'])
                print(f"Wylosowano kolor: {colours_result}")

                # Sprawdzenie, czy użytkownik wygrał czy przegrał
                if user_colour == colours_result:
                    print(f"Wygrałeś kolor! 🎉 i {2 * user_money} zł")
                    balance += 2 * user_money
                else:
                    print("Przegrałes 😔")

                break

            else:
                print('podaj kolor czerwony lub czarny')

    print(f"Saldo po grze: {balance} zł")

# pytanie gracza czy chce grac dalej
    answer = input("czy chcesz grac dalej? (t/n)")
    if answer == "n":
        break
