from termcolor import colored, cprint, COLORS

personen = int(input("Hoeveel personen?: "))
toegangsticket = float(input("Hoeveel kost het toegangsticket (in euro's)?: "))
vip_vr = float(input("Hoeveel kost het VIP VR per minuut (in euro's)?: "))
vip_vr_tijd = int(input("Hoeveel VIP VR tijd (in minuten)?: "))
resultaat = (toegangsticket * personen)
resultaat2 = (vip_vr * vip_vr_tijd)
prijs = resultaat + resultaat2

personen_colored = colored(personen, 'blue')
toegangsticket_colored = colored(toegangsticket, 'red')
vip_vr_colored = colored(vip_vr, 'green')
vip_vr_tijd_colored = colored(vip_vr_tijd, 'grey')
resultaat_colored = colored(resultaat, 'yellow')
resultaat2_colored = colored(resultaat2, 'light_cyan')
prijs_colored = colored(prijs, 'light_magenta')

print(f"Dit geweldige dagje-uit met {personen_colored} mensen in de Speelhal met {vip_vr_tijd_colored} minuten VR kost je maar {prijs_colored} euro")