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


def int_checker(low_num, high_num, question, error1, error2, error3):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response < low_num:
                print(error2)
                break
            elif response >= high_num:
                print(error3)
                break
            else:
                return response
                valid = True
        except ValueError:
            print(error1)


tickets = 5

while tickets != 0:
    print("You have {} tickets remaining".format(tickets))
    name = not_blank("What is your name?: ", "This can't be blank please enter a name.")
    if name == "xxx":
        tickets = 0
        break
    age = int_checker(12, 130, "What is your age?: ", "This has to be a whole number", "You are too young for this movie", "That is very old is this a mistake?")
    tickets -= 1
    if tickets == 0 and name != "xxx":
        print("You have sold all remaining tickets")
