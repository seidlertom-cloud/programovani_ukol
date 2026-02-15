# Převod čísla na římské číslice a zpět
# Tomáš Seidler, 2.ročník
# Úvod do programování (MZ370P19), zimní semestr 2025/2026



# Funkce pro převod arabských čísel na římské číslice
def arabic_to_roman(number):
    # Slovník ve sestupném pořadí (hodnota: římský symbol)
    roman_values = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    # Proměnná pro uložení výsledného římského čísla (string)
    result = ""
    
    # Cyklus for procházející hodnoty v slovníku (který je seřazený sestupně)
    for value in roman_values:
        # Počet kolikrát se hodnota vejde do zadaného čísla
        count = number // value # "//" pro celočíselné dělení
        # Přidání odpovídajícího počtu římských symbolů do výsledné proměnné
        result += roman_values[value] * count
        # Odečtení hodnoty (přičteného římského symbolu) od zadaného čísla
        number -= value * count
    # Vrátí výsledné římské číslo jako string
    return result



# Funkce pro převod římských číslic na arabské číslo
def roman_to_arabic(roman):
    # Slovník pro převod římských číslic na arabské hodnoty
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Proměnná pro uložení výsledného arabského čísla (integer)
    total = 0
    # Délka zadaného římského čísla
    n = len(roman)
    # Cyklus for procházející každý charakter v zadaném římském čísle
    for i in range(n):
        # Arabská hodnota pro aktuální římský symbol
        current_value = roman_values[roman[i]]
        # Kontrola zda aktuální symbol nemá menší hodnotu než následující
        if i < n - 1 and current_value < roman_values[roman[i + 1]]:
            total -= current_value
        else:
            # Jinak přičteme hodnotu římského symbolu k celkovému součtu
            total += current_value
    # Vrátí výsledné arabské číslo jako integer
    return total



# Hlavní část programu
print("Program pro převod arabských čísel na římské.")
while True:
    vstup = input("Zadejte arabské kladné celé číslo v rozsahu 1 až 4000 "
                  "pro převod na římské číslo nebo 'konec' pro ukončení programu (pište bez mezer): \n"
                  ).strip() 
    # Kontrola zda uživatel zadal "konec" pro ukončení programu
    if vstup.lower() == 'konec':
        print("Konec programu.")
        break
    # Kontrola zda je vstupní hodnota číslo (kladné celé číslo)
    if vstup.isdigit():
        arabic_number = int(vstup)
        if not 1 <= arabic_number <= 4000: # Kontrola zda je zadané číslo v požadovaném rozsahu
            print("Zadejte kladné celé číslo v rozsahu 1 až 4000.")
            continue
        roman_number = arabic_to_roman(arabic_number)
        print(f"Římské číslo pro {arabic_number} je: {roman_number}")
        print(f"Převod zpět na arabské číslo: {roman_to_arabic(roman_number)}")
    else:
        # Pokud vstup není číslo, zobrazí chybovou zprávu
        print("Neplatný vstup. Zadejte kladné celé číslo v rozsahu 1 až 4000 nebo 'konec'.") 


