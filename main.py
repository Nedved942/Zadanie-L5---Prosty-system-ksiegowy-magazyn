print("\n*** Prosty system księgowy/magazyn ***\n")

print("Witaj w programie księgowo-magazynowym.")

amount_in_account = 0  # Stan konta
warehouse = {}  # Słownik - magazyn
operation_history = []

while True:
    menu_command = input("""
Wybierz jedno z poniższych poleceń (możesz wpisać także numer):
1 - saldo
2 - sprzedaż
3 - zakup
4 - konto
5 - lista
6 - magazyn
7 - przegląd
8 - koniec
""")

    # TODO Pytanie do konsultacji: Czy powyżej stosuje się taki zapis z """ x ""?
    #  Nie podoba mi się to wcięcie na pierwszym poziomie. Jest nieczytelne.

    # TODO Pytanie do konsultacji: Poniżej instrukcja switch?

    if menu_command == "1" or menu_command == "saldo":
        # Dodanie lub odjęcie wartości od kwoty na koncie
        difference_in_account = input("Podaj kwotę do dodania lub odjęcia z konta: ")
        difference_in_account = float(difference_in_account)
        amount_in_account = amount_in_account + difference_in_account

        # Aktualizacja historii operacji
        operation_history.append({"Saldo":
                                      (
                                          f"Kwota operacji: {difference_in_account}",
                                          f"Stan konta po operacji: {amount_in_account}"
                                      )})

    elif menu_command == "2" or menu_command == "sprzedaż":
        # Wprowadzenie danych
        product_to_sell_name = input("Podaj nazwę produktu, który chcesz sprzedać: ")
        if product_to_sell_name not in warehouse:
            print("Produkt, który chcesz sprzedać nie występuje w magazynie.")
            break
        product_to_sell_price = input("Podaj cenę sprzedaży danego produktu: ")
        product_to_sell_price = float(product_to_sell_price)
        product_to_sell_amount = input("Podaj ilość produktów do sprzedania: ")
        product_to_sell_amount = int(product_to_sell_amount)

        # Odjęcie z magazynu sprzedawanej ilości towaru
        warehouse[product_to_sell_name]["amount"] = \
            warehouse[product_to_sell_name]["amount"] - product_to_sell_amount

        # Sprawdzenie czy jest wystarczająca ilość towaru w magazynie
        if warehouse[product_to_sell_name]["amount"] < 0:
            product_to_sell_amount = product_to_sell_amount + \
                                     warehouse[product_to_sell_name]["amount"]
            print(f"Brak wystarczającej ilości danego towaru w magazynie. "
                  f"Sprzedano {product_to_sell_amount} sztuk.")
            warehouse[product_to_sell_name]["amount"] = 0

        # Dodanie do konta kwoty sprzedaży
        amount_in_account = amount_in_account + (product_to_sell_price * product_to_sell_amount)

        # Jeśli ilość danego towaru = 0 usunięcie towaru z kartoteki magazynu
        if warehouse[product_to_sell_name]["amount"] == 0:
            del warehouse[product_to_sell_name]

        # Aktualizacja historii operacji
        operation_history.append({"Sprzedaż":
                                      (
                                          f"Nazwa sprzedanego produktu: {product_to_sell_name}",
                                          f"Kwota sprzedaży za jeden produkt: {product_to_sell_price}",
                                          f"Ilość sprzedanych produktów: {product_to_sell_amount}",
                                          f"Stan konta po operacji: {amount_in_account}"
                                      )})

    elif menu_command == "3" or menu_command == "zakup":
        # Wprowadzenie danych
        product_to_buy_name = input("Podaj nazwę zakupionego produktu: ")
        if product_to_buy_name in warehouse:
            # noinspection PyTypeChecker
            product_to_buy_price = warehouse[product_to_buy_name]["price"]
            print("Cena produktu wynosi: ", warehouse[product_to_buy_name]["price"])
            user_answer = input("Chcesz ją nadpisać? y/n: ")
            if user_answer == "y":
                product_to_buy_price = input("Podaj cenę zakupionego "
                                             "produktu (pojedynczego): ")
            elif user_answer == "n":
                pass
            else:
                print("Niewłaściwa komenda.")
        else:
            product_to_buy_price = input("Podaj cenę zakupionego "
                                         "produktu (pojedynczego): ")
        product_to_buy_price = float(product_to_buy_price)
        product_to_buy_amount = input("Podaj ilość zakupionych produktów: ")
        product_to_buy_amount = int(product_to_buy_amount)

        # Sprawdzenie wystarczających środków na końcie i aktualizacja stanu konta
        if (product_to_buy_price * product_to_buy_amount) > amount_in_account:
            print("Koszt zakupu większy od stanu konta. Operacja niemożliwa.")
            continue
        else:
            amount_in_account = amount_in_account -\
                                (product_to_buy_price * product_to_buy_amount)

        #  Sprawdzenie czy dany produkt jest już w magazynie.
        #  Jeśli tak, zwiększenie jego ilości.
        if product_to_buy_name in warehouse:
            warehouse[product_to_buy_name]["amount"] = warehouse[product_to_buy_name]["amount"] \
                                                       + product_to_buy_amount
        else:
            # Dodanie produktu do słownika magazynu
            warehouse[product_to_buy_name] = {
                "price": product_to_buy_price,
                "amount": product_to_buy_amount
            }

        # Aktualizacja historii operacji
        operation_history.append({"Zakup":
                                      (
                                          f"Nazwa zakupionego produktu: {product_to_buy_name}",
                                          f"Kwota zakupu za jeden produkt: {product_to_buy_price}",
                                          f"Ilość zakupionych produktów: {product_to_buy_amount}",
                                          f"Stan konta po operacji: {amount_in_account}"
                                      )})

    elif menu_command == "4" or menu_command == "konto":
        # Wyświetla aktualny stan konta
        print("Kwota na koncie wynosi: ", amount_in_account)

        # Aktualizacja historii operacji
        operation_history.append("Konto")

    elif menu_command == "5" or menu_command == "lista":
        # Wyświetla całkowity stan magazynu
        print("Stan magazynu: ")
        for index, name in enumerate(warehouse):
            print(f"{index + 1}. {name.capitalize()}:\n"
                  f"  cena: {warehouse[name]['price']}\n"
                  f"  ilość: {warehouse[name]['amount']}")

        # Aktualizacja historii operacji
        operation_history.append("Lista")

    elif menu_command == "6" or menu_command == "magazyn":
        # Wyświetla ilość wskazanego produktu
        product_to_display = input("Podaj nazwę produktu do wyświetlenia: ")
        print(f"Ilość powyższego produktu w magazynie to "
              f"{warehouse[product_to_display]['amount']} szt.")

        # Aktualizacja historii operacji
        operation_history.append("Magazyn")

    elif menu_command == "7" or menu_command == "przegląd":
        # Wyświetla historię operacji
        print("Historia operacji:")
        for index, operation in enumerate(operation_history):
            print(f"{index + 1}. {operation}")

        # Aktualizacja historii operacji
        operation_history.append("Przegląd")

    elif menu_command == "8" or menu_command == "koniec":
        break

    else:
        pass
