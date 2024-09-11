from termcolor import colored, cprint, COLORS
croissantjes = int(input("Hoeveel croissantjes?: "))
prijs_croissant = float(input("Wat kosten de croissantjes (in euro's)?: "))
stokbroden = int(input("Hoeveel stokbroden?: "))
prijs_stokbroden = float(input("Wat kosten de stokbroden (in euro's)?: "))
kortingsbonnen = int(input("Hoeveel kortingsbonnen heeft u?: "))
korting = int(kortingsbonnen * 0.50)
feestlunch = int((croissantjes * prijs_croissant) + (stokbroden * prijs_stokbroden) - korting )

croissantjes_colored = colored(croissantjes, 'blue')
prijs_croissant_colored = colored(prijs_croissant, 'red')
stokbroden_colored = colored(stokbroden, 'green')
prijs_stokbroden_colored = colored(prijs_stokbroden, 'light_magenta')
kortingsbonnen_colored = colored(kortingsbonnen, 'light_blue')
korting_colored = colored(korting, 'light_red')
feestlunch_colored = colored(feestlunch, 'cyan')

print(f"De feestlunch kost je bij de bakker {feestlunch_colored} euro voor de {croissantjes_colored} croissantjes en de {stokbroden_colored} stokbroden als de {kortingsbonnen_colored} kortingsbonnen nog geldig zijn!")