car_rental = input("What kind of car you would like: ")
print(f"\tLet me see if I can find you a {car_rental}")
dinner = input("Hi, how many people in you dinner group: ")
dinner = int(dinner)
if dinner > 8:
    print("\tNot enough tables for now. could you please wait a little bit")
else:
    print("\tYour table is ready!")

travel = "Please enter the name of a city you have visited:"
travel += "(Enter 'quit' when you are finished)"
while True:
    city = input(travel)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

promt = "\nPlease, choose topping for your pizza"
promt += "\nEnter 'quit' when you finished chooosing pizza toppings: "
while True:
    pizza = input(promt)
    if pizza == 'quit':
        break
        print("You order will be ready soon. Thank you")
    else:
        print("We added topping to your pizza")

promt = "\nWhat is you age: "
active = True
while active:
    message = input(promt)
    message = int(message)
    if message == 123:
        active = False
    elif message <= 3:
        print('Your ticket is free!')
    elif message > 3 and message <= 12:
        print("Ticket is 10$")
    elif message > 12:
        print("Ticket is 15$")
    else:
        print(message)

number = 0
while number < 100:
    number += 1
    if number % 2 == 0:
        continue
    print(number)

sandwich_orders = ['tuna','veggie','chicken tariyaki','steak','pastrami','tuna','steak','pastrami','pastrami']
finished_sandwiches = []
print("\nThe deli ran out of pastrami")
while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    current_order = sandwich_orders.pop()
    print(f"\nI made you {current_order}")
    finished_sandwiches.append(current_order)
print("\nThe following sandwiches were made: ")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response
    repeat = input("Would anyone else to answer? ")
    if repeat == 'no':
        polling_active = False
print("---Poll Results---")
for name, response in responses.items():
    print(f"{name.title()} favorite's place to go {response.title()}")
