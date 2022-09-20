def string_check(question, to_check):
    valid = False
    while not valid:
        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:

                if response == item[0]:
                    return item
        print("Please enter either Yes or No")


for item in range(0, 6):
    snack_question = string_check("Would you like snacks? ", ["yes", "no"])
    print("Your answer was {} to snacks".format(snack_question))
