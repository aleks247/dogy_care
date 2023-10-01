supposed_kg_food = int(input("Enter your suppose for the food: "))

kg_food_price = 5.50

final_food = 0

while True: 
    command = input("Enter daily food intake (grams): ")
 
    if command.lower() == 'stop':
        if final_food <= supposed_kg_food * 1000:
            leftovers = supposed_kg_food * 1000 - final_food
            spent_price = leftovers / 1000 * kg_food_price
            print(f"Food is enough! Leftovers: {leftovers} grams")
            print(f"So you spent {spent_price:.2f} leva for food.")
        else:
            needed_food = final_food - supposed_kg_food * 1000
            spent_price = (needed_food / 1000) * kg_food_price
            print(f"Food is not enough. You need {needed_food} grams")
            print(f"So you need {spent_price:.2f} more leva for food.")
        break
    elif command.isdigit():
        final_food += int(command)
    else: 
        print("Wrong input!")
