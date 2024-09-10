croissantjes = 17
prijs_croissant = 0.39
stokbroden = 2
prijs_stokbroden = 2.78
kortingsbonnen = 3
korting = kortingsbonnen * 0.50
feestlunch = (croissantjes * prijs_croissant + stokbroden * prijs_stokbroden - korting )
print(f"De feestlunch kost je bij de bakker {feestlunch} euro voor de {croissantjes} croissantjes en de {stokbroden} stokbroden als de {kortingsbonnen} kortingsbonnen nog geldig zijn!")