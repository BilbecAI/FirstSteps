uczniowie = {
    "uczen_1": {"Imie":"Dawid", "Wiek": 15, "Oceny": [4, 5, 3]},
    "uczen_2": {"Imie":"Anna", "Wiek": 16, "Oceny": [5, 5, 4]}
}
def wypisz_uczniow(uczniowie):
    for uczen,dane in uczniowie.items():
        print (f"{uczen}, Imie: {dane['Imie']}\n\tWiek:{dane['Wiek']}, Oceny:{dane['Oceny']} ") 
wypisz_uczniow(uczniowie)
odp=input("Jeśli chcesz dodać nowego ucznia napisz: Tak")
if odp=='Tak':
    nowe_imie=input("Wprowadz Imie ucznia: ")
    nowy_wiek=(int(input("Wprowadz wiek ucznia:")))
    nowe_oceny=input("Wprowadz oceny:")
    nowe_oceny=list(map(int, nowe_oceny.split()))
    nowy_id = f"uczen_{len(uczniowie) + 1}"
uczniowie[nowy_id]= {"Imie": nowe_imie, "Wiek": nowy_wiek, "Oceny": nowe_oceny}
wypisz_uczniow(uczniowie)
uczen_znaleziony=input("Podaj imie ucznia którego chcesz znaleźć: ")
for uczen,dane in uczniowie.items():
    if uczen_znaleziony in {dane['Imie']}:
        print (f"{uczen}, {dane['Imie']} \n\t Wiek: {dane['Wiek']} \n\t Oceny: {dane['Oceny']}")
uczen_usuniety=input("Podaj imię ucznia którego chcesz usunąć:")
uczen_znaleziony=False
for uczen in list(uczniowie.keys()):
    if uczniowie[uczen]['Imie']==uczen_usuniety:
        del uczniowie[uczen]
        print(f"Uczeń {uczen_usuniety} został usunięty")
        uczen_znaleziony=True
        break
if not uczen_znaleziony:
    print(f"Nie ma ucznia o imieniu {uczen_usuniety}")
wypisz_uczniow(uczniowie)

