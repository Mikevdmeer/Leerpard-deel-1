Vraag1 = input("Is de kaas geel? Ja/Nee: ")
if Vraag1 == ("Ja"):
    Vraag2 = input("Zitten er gaten in? Ja/Nee: ")
    if Vraag2 == ("Ja"):
        Vraag3 = input("Is de kaas belachelijk duur? Ja/Nee: ")
        if Vraag3 == ("Ja"):
            print("Emmenthaler")
    elif Vraag2 == ("Nee"):
        Vraag4 = input("Is de kaas hard als steen? Ja/Nee: ")
        if Vraag4 == ("Ja"):
            print("Leerdammer")
        else: print("Goudse kaas")
elif Vraag1 == ("Nee"):
    Vraag5 = input("Heeft de kaas blauwe schimmel? Ja/Nee: ")
    if Vraag5 == ("Ja"):
        Vraag6 = input("Heeft de kaas korst? Ja/Nee: ")
        if Vraag6 == ("Ja"):
            print("Blue de Rochbaron")
        elif Vraag6 == ("Nee"):
            print("Foume d'ambert")
    elif Vraag5 == ("Nee"):
        Vraag7 = input("Heeft de kaas korst? Ja/Nee: ")
        if Vraag7 == ("Ja"):
            print("Camembert")
        else:
            print("Mozzarella")