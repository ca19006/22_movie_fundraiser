def not_blank(question, error):
    # Adding a loop so that the program doesn't continue if the input is blank
    valid = False
    while not valid:
        # adding the question that is going to be asked
        response = input(question)
        # If the response is not blank and the response will be returned to the main routine
        if response != "":
            return response
        # If the response is blank the program will print an error message
        else:
            print(error)


def int_checker(question):
    error = "Please enter a whole number between 12 and 130"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


name = ""
tickets = 0
max_tickets = 7
ticket_sale = 0
ticket_price = 0
profit_made = 0
profit = 0

while name != "xxx" and tickets < max_tickets:
    if tickets < max_tickets - 1:
        print("You have {} tickets left".format(max_tickets - tickets))
    else:
        print("You have one place left")

    name = not_blank("Name: ", "This can't be blank please enter your name")
    if name == "xxx":
        break

    age = int_checker("Age: ")
    if age < 12:
        print("You are too young for this movie")
        continue
    elif age > 130:
        print("That is very old it looks like a mistake")
        continue
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    tickets += 1
    ticket_sale += ticket_price
    print("Your ticket price is ${:.2f}".format(ticket_price))
    profit_made = ticket_price - 5
    print("you made ${:.2f} profit".format(profit_made))
    profit += profit_made
    ticket_price = 0
print("You made ${:.2f} profit".format(profit))
