BTW_PERC = 21
aantal = 7
prijs = 3.78
korting = 1
item='ballonnen'
 
kosten = aantal * prijs - korting
btw = kosten * BTW_PERC / (100 + BTW_PERC)
bon = f'item: {item}: kosten: {kosten:.2f} btw: {btw:.2f}'

TAX_PERC = 0.36
salary = 2300.0
employees = 5
 
value = (salary * employees) * (1 - TAX_PERC)

length = len(str("6.17"))


result = '12.4 - 5'
amount = 555
6.34 * str(amount)
print(amount)