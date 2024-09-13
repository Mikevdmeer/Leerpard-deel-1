gastheer = True
gasten = True
drank = True
chips = True

#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
start_condition_2 = gastheer or (gasten and chips and drank)
start_condition_3 = not (chips and not drank)
start_condition_4 = not (gasten and (not chips or not drank))
start_condition_5 = gastheer and drank
start_condition_6 = not (chips and not gasten and not gastheer)
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