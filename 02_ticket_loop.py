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


tickets = 5

while tickets != 0:
    print("You have {} tickets remaining".format(tickets))
    name = not_blank("What is your name?: ", "This can't be blank please enter a name.")
    tickets -= 1
    if name == "xxx":
        tickets = 0
    if tickets == 0 and name != "xxx":
        print("You have sold all remaining tickets")
