print("Welcome To Temp Converter!")
print("1. Convert F to C")
print("2. Convert C to F")
choice = input("1 or 2? ")
if (int(choice) == 1):
    temp_f = input("What Is The Temp (F)? ")
    temp_c = (float(temp_f) - 32) * (5/9)
    print("The Temp Is " , temp_c , " (C)")  
elif (int(choice) == 2):
    ask_c = input("What Is The Temp (C)")
    ask_f = (float(ask_c) * (9/5)) + 32
    print("The Temp Is " , (ask_f) , " (F)")
else:
    print("Incorrect Number Please Try Again")