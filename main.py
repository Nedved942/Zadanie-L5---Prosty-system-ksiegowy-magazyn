print("\n*** Prosty system księgowy/magazyn ***\n")

print("Witaj w programie księgowo-magazynowym.")

amount_in_account = 0  # Stan konta
warehouse = {}  # Słownik - magazyn

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

    # TODO Pytanie do konsultacji: Czy powyżej stosuje się taki zapis z """ x ""? Nie podoba mi się to wcięcie na
    # TODO pierwszym poziomie. Jest nieczytelne.

    # TODO Pytanie do konsultacji: Poniżej instrukcja switch?

    if menu_command == "1" or menu_command == "saldo":
        difference_in_account = input("Podaj kwotę do dodania lub odjęcia z konta: ")
        difference_in_account = int(difference_in_account)
        amount_in_account = amount_in_account + difference_in_account

    elif menu_command == "2" or menu_command == "sprzedaż":
        pass

    elif menu_command == "3" or menu_command == "zakup":
        product_name = input("Podaj nazwę zakupionego produktu: ")
        product_price = input("Podaj cenę zakupionego produktu (pojedynczego): ")
        product_price = int(product_price)
        product_amount = input("Podaj ilość zakupionych produktów: ")
        product_amount = int(product_amount)

        # Sprawdzenie wystarczających środków na końcie i aktualizacja stanu konta
        if (product_price * product_amount) > amount_in_account:
            print("Koszt zakupu większy od stanu konta. Operacja niemożliwa.")
            continue
        else:
            amount_in_account = amount_in_account - (product_price * product_amount)

        # # Dodanie produktu do słownika magazynu
        # warehouse = {
        #     product_name: {
        #         "price": product_price,
        #         "amount": product_amount
        #     }
        # }

    elif menu_command == "4" or menu_command == "konto":
        print("Kwota na koncie wynosi: ", amount_in_account)

    elif menu_command == "5" or menu_command == "lista":
        pass

    elif menu_command == "6" or menu_command == "magazyn":
        pass

    elif menu_command == "7" or menu_command == "przegląd":
        pass

    elif menu_command == "8" or menu_command == "koniec":
        break

    else:
        pass
