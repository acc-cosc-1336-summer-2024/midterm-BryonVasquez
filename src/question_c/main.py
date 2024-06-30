#add import 
def main(): 
    while True: 
        try: 
            sales = float(input("Enter the sales amount: ")) 
            bonus = get_bonus_pay_amount(sales) 
            if bonus == 'Invalid argument': 
                print(bonus) 
            else: 
                print(f"The bonus pay amount is: {bonus}") 
            break 
        except ValueError: 
            print("Invalid input. Please enter a valid number. ") 