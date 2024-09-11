naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslacht = input("Ben je een A) een jonge of B) een meisje? ").lower()
fav_kleur = input("Wat is je favoriete kleur? ")
fav_getal = int(input("Wat is je favoriete getal? "))
rekensom = abs(leeftijd-fav_getal)
haar_of_zijn = 'haar' if geslacht == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{haar_of_zijn.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", fav_kleur)
print(f"Het verschil tussen {haar_of_zijn} leeftijd en {fav_getal} is:", rekensom)
