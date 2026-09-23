temps = []
while(True):
    print("Select an option from the following")
    menu = """
    1. Add a temp
    2. list temp
    3. calc avg
    4. exit
    """
    print(menu)
    select = float(input("Enter a selection: "))

    if (select == 1):
        temp = float(input("enter temp"))
        temps.append(temp)
    elif(select == 2):
        print(temps)
    elif(select == 3):
        total = 0
        for temp in temps:
            total += temp
        avg = total / len(temps)
        print(f"Average Temp: {avg}")
        input("Hit Emter To Continue")
    elif(select == 4):
        exit()
    else:
        print("Wrong Amnswer Bitch (Stewie Griffin Voice) ")
        exit()