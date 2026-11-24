name = input("What is your name? ")
age = input("How old are you? ")
train = input("How Many Years Have You Been Training? ")
color = input("What is your favorite color? ")
tool = input("How Many Gadgets Are You Carring? ")
min = input("How Many Minutes Do You Have To Complete The Mission? ")
travel = input("How Many Minutes Do You Have To Travel? ")
training_percentage = int(train) / int(age) * 100
gadget_density = int(tool) / int(train) 
mission_seconds = int(min) / 60
mission_time_remaining = int(min) - int(travel)
mission_code = f"{name}-{color}-{age}"
print(f"Mission Code: {mission_code}")
if int(age) <= 18:
    adult = False
else:
    adult = True
if int(tool) <= 5:
    gadgets = False
else:
    gadgets = True
if int(train) >= 0:
    rookie = True
else:
    rookie = False
print(f"Hello {name}, you are {age} years old and have been training for {train} years. Your favorite color is {color}. You are carrying {tool} gadgets. You have {min} minutes to complete the mission, with {travel} minutes of travel time. Your training percentage is {training_percentage:.2f}% and your gadget density is {gadget_density:.2f}. The mission code is: {mission_code}. You are an adult: {adult}. You have enough gadgets: {gadgets}. You are a rookie: {rookie}. Good Luck. ")