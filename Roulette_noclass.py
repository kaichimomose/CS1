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
bet_even_odd = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def take_bet(color, number, evenodd, amount):
    bet_color = color
    bet_number = number
    bet_amount = amount
    bet_even_odd = evenodd
    return [bet_color, bet_number, bet_even_odd, bet_amount]


def roll_ball():
    # returns a random number between 0 and 37
    return random.randint(0, 37)


def check_results(bet, number_result):
    # Compares bet_color to color rolled. Compares bet_number to number_rolled.
    color_result = None
    evenodd_result = None
    if number_result in red:
        color_result = "red"
    else:
        color_result = "black"
    if number_result != 0:
        if number_result % 2 == 0:
            evenodd_result = "even"
        else:
            evenodd_result = "odd"
    else:
        evenodd_result = evenodd_result
    print("Boll number is %s, it is %s and Color is %s" % (number_result, evenodd_result, color_result))
    if bet[2] == evenodd_result:
        if bet[0] == color_result:
            if bet[1] == number_result:
                return [True, True, True]  # [evenodd, color, number]
            else:
                return [True, True, False]
        else:
            if bet[1] == number_result:
                return [True, False, True]
            else:
                return [True, False, False]
    else:
        if bet[0] == color_result:
            if bet[1] == number_result:
                return [False, True, True]
            else:
                return [False, True, False]
        else:
            if bet[1] == number_result:
                return [False, False, True]
            else:
                return [False, False, False]


def payout(check, bet):
    # returns total amount won or lost by user based on results of roll.
    if check[0] is True:
        if check[1] is True:
            if check[2] is True:
                return bet[3] * 2 * 2 * 38
            else:
                return bet[3] * 2 * 2
        else:
            if check[2] is True:
                return bet[3] * 2 * 38
            else:
                return bet[3] * 2
    else:
        if check[1] is True:
            if check[2] is True:
                return bet[3] * 2 * 38
            else:
                return bet[3] * 2
        else:
            if check[2] is True:
                return bet[3] * 38
            else:
                if bet[3] is None:
                    return 0
                else:
                    return -(bet[3])


def confirm_amount():
    amount = input("Amount: ")
    if amount != "":
        amount = int(amount)
        if amount < 10:
            print("Minimum bet is $10.")
            amount = confirm_amount()
        elif amount > bank_account:
            print("You do not have that much money.")
            amount = confirm_amount()
        else:
            print("%s" % amount)
            amount = amount
    else:
        amount = None
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
    print("Decide color(red or black), number(0 ~ 37) and even or odd. Keep it blank if you do not bet.")
    color = input("Color (red or black): ")
    if color != "red" and color != "black" and color != "":
        print("Please choose from red, black or blank")
        play_game()
    else:
        number = input("Number (0 ~ 37): ")
        if int(number) in range(0, 38):
            number = int(number)
        elif number == "":
            number = None
        else:
            print("Please choose a number from 0 to 37 or keep it blank")
            play_game()
        evenodd = input("Even or Odd: ")
        if evenodd == "Even" or evenodd == "even" or evenodd == "Odd" or evenodd == "odd" or evenodd == "":
            evenodd = evenodd
            amount = confirm_amount()
        else:
            print("Even (even), Odd (odd) or Blank")
            play_game()
    bet = take_bet(color, number, evenodd, amount)
    number_result = roll_ball()
    check = check_results(bet, number_result)
    money = payout(check, bet)
    if money > 0:
        print("YOU WON $%s!" % (money))
    elif money == 0:
        print("YOU DID NOT BET!!")
    else:
        print("YOU LOST $%s!" % (-money))
    # continue_bet()


play_game()
