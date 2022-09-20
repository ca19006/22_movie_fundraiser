# Adding a function so that user inputs can't be blank
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


name = not_blank("What is your name?: ", "This can't be blank, Please enter a name")
