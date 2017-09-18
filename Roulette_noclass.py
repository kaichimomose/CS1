import random
# x = random.randint()
random.seed(1)

# from random import randint
# x = randint()

# from random import randint as r
# x = r()
bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def take_bet(color, number, amount):
    bet_color = color
    bet_number = number
    bet_amount = amount
    return [bet_color, bet_number, bet_amount]


def roll_ball():
    # returns a random number between 0 and 37
    return random.randint(0, 37)


def check_results(bet, number_result):
    # Compares bet_color to color rolled. Compares bet_number to number_rolled.
    color_result = None
    if number_result in red:
        color_result = "red"
    elif number_result in black:
        color_result = "black"
    else:
        color_result = "green"
    print("Boll number is %s, and Color is %s" % (number_result, color_result))
    if bet[0] == color_result:
        if bet[1] == number_result:
            return [True, True]
        else:
            return [True, False]
    else:
        if bet[1] == number_result:
            return [False, True]
        else:
            return [False, False]


def payout(check, bet):
    # returns total amount won or lost by user based on results of roll.
    if check[0] is True:
        if check[1] is True:
            return bet[2] * 2 * 38
        else:
            return bet[2] * 2
    else:
        if check[1] is True:
            return bet[2] * 2
        else:
            return -(bet[2])


def confirm_amount():
    amount = int(input("Amount: "))
    if amount < 10:
        print("Minimum bet is $10.")
        amount = confirm_amount()
    elif amount > bank_account:
        print("You do not have that much money.")
        amount = confirm_amount()
    else:
        print("%s" % amount)
        amount = amount
    return amount


# def continue_bet():
#     yes_or_no = input("Continue? Yes or No: ")
#     if yes_or_no == "Yes" or yes_or_no == "yes":
#         play_game()
#     elif yes_or_no == "No" or yes_or_no == "no":
#         pass
#     else:
#         print("Excuse me. Say again please?")
#         continue_bet()


def play_game():
    # This is the main function for the game.
    # When this function is called, one full iteration of roulette, including:
    # Take the user's bet. Roll the ball. Determine if the user won or lost.
    # Pay or deduct money from the user accordingly.
    color = input("Color: ")
    if color != "red" and color != "black" and color != "green":
        print("Please choose from red, black or green")
        play_game()
    else:
        number = int(input("Number: "))
        if number in range(0, 38):
            number = number
            amount = confirm_amount()
        else:
            number = None
            amount = confirm_amount()
    bet = take_bet(color, number, amount)
    number_result = roll_ball()
    check = check_results(bet, number_result)
    print("%s" % bet)
    money = payout(check, bet)
    if money > 0:
        print("YOU WON $%s!" % (money))
    else:
        print("YOU LOST $%s!" % (-money))
    # continue_bet()


play_game()
