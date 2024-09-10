from termcolor import colored, cprint, COLORS

personen = 4
toegangsticket = 7.45
vip_vr = 0.37
vip_vr_tijd = 45
resultaat = (toegangsticket * personen)
resultaat2 = (vip_vr * vip_vr_tijd)
prijs = resultaat + resultaat2

personen_colored = colored(personen, 'blue')
toegangsticket_colored = colored(toegangsticket, 'red')
vip_vr_colored = colored(vip_vr, 'green')
vip_vr_tijd_colored = colored(vip_vr_tijd, 'grey')
resultaat_colored = colored(resultaat, 'yellow')
resultaat2_colored = colored(resultaat2, 'light_cyan')
prijs_colored = colored(prijs, 'white')

print(f"Dit geweldige dagje-uit met {personen_colored} mensen in de Speelhal met {vip_vr_tijd_colored} minuten VR kost je maar {prijs_colored} euro")