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


def play_game(color, number, amount):
    # This is the main function for the game.
    # When this function is called, one full iteration of roulette, including:
    # Take the user's bet. Roll the ball. Determine if the user won or lost.
    # Pay or deduct money from the user accordingly.
    bet = take_bet(color, number, amount)
    number_result = roll_ball()
    check = check_results(bet, number_result)
    print("%s" % payout(check, bet))


play_game("black", 4, 500)
