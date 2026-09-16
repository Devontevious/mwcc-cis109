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
print(mission_code)