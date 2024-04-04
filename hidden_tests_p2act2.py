def sol_get_average():
    """This function prompts the user to input numbers, once they're done they should type "stop" and
    then prints out a message with the average of the valid numbers the user typed in. """
    ### BEGIN SOLUTION
    total = 0
    count = 0
    while True:
        num = input("Input a number. Type 'stop' to stop: ")
        if num == "stop":
            break
        try:
            x = float(num)
            total += float(num)
            count += 1
        except:
            print("Invalid input. Please try again.")
    if count == 0:
        print("No valid numbers were given.")
    else:
        print("The average is: " + str(total/count))
    return
    ### END SOLUTION

def input_get_average(num_tests=30):
    from random import choices, choice
    lens = [i for i in range(5)]
    options = [str(i) for i in range(0, 10)] + ['one', 'st', 'fshdjs', 'five', 'top']
    input_values = [choices(options, k=choice(lens)) + ['stop'] for i in range(num_tests)]
    input_values.append(["stop"])
    input_args = [{} for i in range(num_tests+1)]
    return input_values, input_args

def sol_calculate_tip():
    """This function asks the user to input the restaurant ticket price and their level of satisfaction and
    prints out what the tip should be based on their level of satisfaction with the service. """
    ### BEGIN SOLUTION
    while True:
        ticket_price = input("Input the ticket price: ")
        try: 
            ticket_price = float(ticket_price)
        except:
            print("The ticket price must be a numeric value. Please try again.")
            continue
        if ticket_price >= 0:
            break
        print("The ticket price must be a positive number. Please try again.")
    acceptable_options = ["0", "1", "2", "3", "4", "5"]
    while True:
        satisfaction_level = input("Input the level of satisfaction: ")
        if satisfaction_level in acceptable_options:
            break
        print("The satisfaction level should be 0, 1, 2, 3, 4 or 5. Please try again.")
    satisfaction_dict = {"0":0, "1":0.05, "2":0.1, "3":0.15, "4":0.2, "5":0.3}
    tip = ticket_price*satisfaction_dict[satisfaction_level]
    print("The tip should be: " + str(tip))
    return

def input_calculate_tip(num_tests=20):
    from random import choice, choices
    negative_prices = [str(i) for i in range(-100, -1, 10)]
    invalid_prices = ["fivehundred", "jkfds", "two hundred"]
    correct_prices = [str(i) for i in range(10, 500, 10)]
    ### generate the price input values. Some with mistakes in there. 
    prices = [[choice(correct_prices)] for i in range(10)]
    prices += [choices(negative_prices, k=choice([1, 2, 3, 4])) + [choice(correct_prices)] for i in range(num_>
    prices += [choices(invalid_prices, k=choice([1, 2, 3, 4])) + [choice(correct_prices)] for i in range(3)]
    ### generate satisfaction input values, some with mistakes in there. 
    correct_satisfaction = ["0", "1", "2", "3", "4", "5"]
    incorrect_satisfaction = ["one", "bad", "no"]
    satisfactions = [[choice(correct_satisfaction)] for i in range(15)]
    satisfactions += [choices(incorrect_satisfaction, k=choice([1, 2, 3, 4])) + [choice(correct_satisfaction)]>
    input_values = []
    for price, satisfaction in zip(prices, satisfactions):
        input_values.append(price+satisfaction)
    input_args = [{} for i in range(20)]
    return input_values, input_args
