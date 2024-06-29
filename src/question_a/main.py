#add import 
def main(): 
    while True: 
        user_input = input("Enter a number (1-7) to get the corresponding day of the week (enter 'quite' to exit): ") 
        if user_input.lower() == 'quit': 
            print("Exiting the program....") 
            break 
        try: 
            day_number = int(user_input) 
            print (get_day_of_week(day_number)) 
        except ValueError: 
            print("Invalid input. Please enter a number or 'quit' to exit.")  

    