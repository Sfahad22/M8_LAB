

import resources

def check_items(number):
    print(f"{resources.fahad.weapons}")
    number1_weapons = ['rope', 'coat', 'first aid kit']
    number2_meal = ['pan','groceries']
    number3_book = ['pen', 'paper', 'idea']
    if number == 1:
        for item in number1_weapons:
            if item not in resources.fahad.weapons:
                print(f"Hey, you don't have {item}")
                return False
            else:
                print("you have everything you need, good luck!") 
                
    
        print(f"(number1_weapons)")
    elif number == 2:
        print(f"(number2_meal)")
    elif number == 3:
        print(f"(number3_book)")
    else:
        print("Btw")

check_items(1)