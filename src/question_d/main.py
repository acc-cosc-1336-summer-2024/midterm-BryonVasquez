#add import 
def main(): 
    while True: 
        try: 
            age = int(input("Enter a person's age (or enter any non-numeric value to quit): ")) 
            category = get_person_category(age) 
            print(f"This person is classified as {category}.") 
            
        except ValueError: 
            print("Invalid input. Program will exit.") 
            break 
