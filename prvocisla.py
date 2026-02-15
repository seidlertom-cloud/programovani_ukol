# Rozklad čísla na součin prvočísel
# Tomáš Seidler, 2.ročník
# Úvod do programování (MZ370P19), zimní semestr 2025/2026



# Funkce pro rozklad čísla na prvočísla
def rozklad_na_prvocisla(n):
    # Seznam pro uložení prvočísel, které jsou dělitelem zadaného čísla
    prvocisla = []
    # Proměnná pro aktuální dělitel (začínáme s nejmenším prvočíslem 2)
    delitel = 2 
    # Cyklus while pokračuje, dokud zadané číslo n není zredukováno na 1
    while n > 1:
        # pokud modulo vráti 0, tak se dělitel přidá do seznamu prvočísel
        # a zadané číslo n se vydělí tímto dělitelem
        while n % delitel == 0:
            prvocisla.append(delitel)
            n //= delitel
        # Pokud nelze n vydělit dělitelem, zvýšíme dělitel o 1 a cyklus pokračuje
        delitel += 1
    # Vrátí seznam prvočísel
    return prvocisla



# Hlavní část programu
print("Program pro rozklad čísla na prvočísla.")
while True:
    vstup = input("Zadejte celé číslo větší než 1 a menší než 1000000 "
                  "nebo 'konec' pro ukončení programu (pište bez mezer): \n").strip()
    # Kontrola zda uživatel zadal "konec" pro ukončení programu
    if vstup.lower() == 'konec':
        print("Konec programu.")
        break
    # Kontrola zda je vstupní hodnota číslo (kladné celé číslo větší než 1 a menší než 1000000)
    if vstup.isdigit():
        cislo = int(vstup)
        if cislo < 2 or cislo > 1000000:
            print("Zadejte celé číslo větší než 1 a menší než 1000000.")
            continue
        rozklad = rozklad_na_prvocisla(cislo)
        print(f"Rozklad čísla {cislo} na součin prvočísel: {cislo} = {' x '.join(map(str, rozklad))}")
    else:
        # Pokud vstup není číslo, zobrazí chybovou zprávu
        print("Neplatný vstup. Zadejte celé číslo větší než 1 a menší než 1000000.")


