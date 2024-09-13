gastheer = input("Wie is de gastheer? ")
gasten = int(input("Hoeveel gasten zijn er? "))

drank = True
chips = True

jouw_naam = "Mike"
slb_naam = "Oorschot"

start_condition_1 = (gastheer != "") and (gasten >= 4) and (gasten <= 20)
start_condition_2 = (gastheer != "") and (gasten >= 4) and (gasten <= 20) and chips and drank
start_condition_3 = not (chips and not drank)
start_condition_4 = not (gasten >= 4 and (not chips or not drank))
start_condition_5 = (gastheer != "") and drank
start_condition_6 = not (chips and not gasten and not (gastheer != ""))

feest_hoe_dan_ook = (gastheer == jouw_naam)
geen_feest_hoe_dan_ook = (gastheer == slb_naam)

if feest_hoe_dan_ook:
    print('Start the Party')

elif geen_feest_hoe_dan_ook:
    print('No Party')

else:
    if start_condition_1:
        print('Start the Party')
    else:
        print('No Party')

    if start_condition_2:
        print('Start the Party')
    else:
        print('No Party')

    if start_condition_3:
        print('Start the Party')
    else:
        print('No Party')

    if start_condition_4:
        print('Start the Party')
    else:
        print('No Party')

    if start_condition_5:
        print('Start the Party')
    else:
        print('No Party')

    if start_condition_6:
        print('Start the Party')
    else:
        print('No Party')
