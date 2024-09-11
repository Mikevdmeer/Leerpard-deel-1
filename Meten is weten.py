a = int(input("Noem getal 1 op: "))
b = int(input("Noem getal 2 op: "))
Max = a
Min = a
if a > b:
    print(f"A is het grootste getal: {Max}")
elif b > a:
    print(f"a is het kleinste getal: {Min}")
else:
    print("a en b zijn even groot")