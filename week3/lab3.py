list = []
import time
while True:
    menu = """
    Welcome to Your Shopping List!
 
    Please make a selection from one of the following options:
 
    1. Add an item to the shopping list.
    2. Display the shopping list.
    3. Display the item count.
    4. Display the first item in the shopping list.
    5. Display the last item in the shopping list.
    6. Clear the shopping list.
    7. Stop
    """
    print(menu)
    choice = int(input("Enter your selection: "))
    if choice == 1:
        item = input("Enter an item to add to the shopping list: ")
        list.append(item)
        time.sleep(1)
    elif choice == 2:
        print(list)
        time.sleep(1)
    elif choice == 3:
        total = len(list)
        print(f"Total items in the shopping list: {total}")
        time.sleep(1)
    elif choice == 4:
        if len(list) > 0:
            print(f"The first item in the shopping list is: {list[0]}")
        else:
            print("The shopping list is empty.")
        time.sleep(1)
    elif choice == 5:
        if len(list) > 0:
            print(f"The last item in the shopping list is: {list[-1]}")
        else:
            print("The shopping list is empty.")
        time.sleep(1)
    elif choice == 6:
        list.clear()
        print("The shopping list has been cleared.")
        time.sleep(1)
    elif choice == 7:
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("SIKE, Thats The Wrong Number OHHHHHHHHHHHHHHHHH")
        time.sleep(4)