# Expense tracker
# Napisz program umożliwiający śledzenie wydatków i przychodów. Użytkownik powinien mieć możliwość:
# dodać wydatek:
# Data
# Na co wydał (np. zakupy spożywcze, gra, telefon itp.)
# kwota
# dodać przychód:
# Data
# Jak zarobił (np. praca, kieszonkowe, prezent itp.)
# kwota
# zobaczyć sumę swoich wydatków
# zobaczyć sumę swoich przychodów
# zobaczyć wydatki i przychody po podaniu daty (użytkownik podaje datę i wyświetlają mu się wszystkie wydatki i przychody z tego dnia - nie sumy tylko operacje z data, kwota i opisem za co/na co)
# zobaczyć różnicę między przychodami a wydatkami

from datetime import date

expenses = []
revenues = []


while True:
    menu = input('MENU: 1.Dodaj wydatek 2.Dodaj przychód 3.Suma wydatków 4.Suma przychodów 5.Wyświetl wydatki i przychody 6. Wyświetl różnicę między przychodami i wydatkami ')

    if menu == "".strip():
        break

    menu = int(menu)
    #  1. dodawanie wydatku
    if menu == 1:

        date_input = input('Podaj datę wydatku rok-miesiąc-dzień: ')
        date_input_object = date.fromisoformat(date_input)
        print(date_input_object)
        item_input = input('Wpisz przedmiot zakupu: ')
        amount_input = float(input('Ile wydałeś?: '))

        expense = {
            'date': date_input_object,
            'item_of_purchase': item_input,
            'amount': amount_input
        }

        print(f"Dodałeś wydatek: {expense}")
        expenses.append(expense)
        print(f"Twoje wydatki: {expenses}")

    # 2. Dodawanie przychodu
    elif menu == 2:
        date_request = input('Podaj datę przychodu rok-miesiąc-dzień: ')
        date_request_object = date.fromisoformat(date_request)
        earning_request = input(
            'Jak zarobiłeś(wypłata, prezent, kieszonkowe): ')
        amount_request = float(input('Ile zarobiłeś?: '))

        revenue = {
            'date': date_request_object,
            'way_of_earning': earning_request,
            'amount': amount_request
        }

        print(f"Dodałeś przychód: {revenue}")
        revenues.append(revenue)
        print(f"Twoje przychody: {revenues}")

    # 3. Wyświetlenie sumy wydatków
    elif menu == 3:
        expenses_total = 0
        for expense in expenses:
            expenses_total += expense.get("amount")
        print(f"Suma Twoich wydatków wynosi: {expenses_total}")

    # 4. Wyświetlenie sumy przychodów
    elif menu == 4:
        revenues_total = 0
        for revenue in revenues:
            amount = revenue.get('amount')
            # if amount is not None:

            # dopisac co po ifie i co po bledzie

            # revenues_total += revenue.get("amount")
            # print(f"Suma Twoich przychodów wynosi: {revenues_total}")

    # 5.  Wyświetlenie wydatków i przychodów
    elif menu == 5:
        user_date = input(
            'Podaj datę, dla której chcesz zobaczyć wydatki i przychody rok-miesiac-dzien')
        user_date_object = date.fromisoformat(user_date)

        print(f"TWOJE WYDATKI NA DZIEŃ {user_date_object} WYNOSZĄ: ")
        for expense in expenses:
            if user_date_object == expense.get("date"):
                print(expense.get('date'), expense.get(
                    'item_of_purchase'), expense.get('amount'))

        print(f"TWOJE PRZYCHODY NA DZIEŃ {user_date_object} WYNOSZĄ: ")
        for revenue in revenues:
            if user_date_object == revenue.get("date"):
                print(revenue.get('date'), revenue.get(
                    'way_of_earning'), revenue.get('amount'))

    # 6. Wyświetlenie różnicy między przychodami a wydatkami
    elif menu == 6:
        expenses_total = 0
        for expense in expenses:
            expenses_total += expense.get("amount")

        revenues_total = 0
        for revenue in revenues:
            revenues_total += revenue.get("amount")

        diff = revenues_total - expenses_total
        print(
            f"Różnica pomiędzy Twoimi zarobkami, a wydatkami wynosi: {diff} zł")

        if diff < 0:
            print("Masz dług!")
