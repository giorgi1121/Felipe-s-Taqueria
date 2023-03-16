menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#make try-except to catch errors
try:
    #variabel cost with value of 0
    cost = 0

    #make a loop
    while True:

        #item from user
        item = input("Item: ").title()

        #make a loop to check if item is in menu or not and if yes print total cost
        for k in menu:
            if k == item:
                cost += menu[k]
                print(f"Total: ${cost}0")

#except EOFError finish program
except EOFError:
    pass
