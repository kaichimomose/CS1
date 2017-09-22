import random
random.seed(2)


guessed_letter_list = []
life = 6
number_words = ""


# pick a word up
def loadWord():
    f = open('hangman_words.txt', 'r')
    wordsList = f.readlines()
    f.close()

    wordsList = wordsList[0].split(' ')
    secretWord = random.choice(wordsList)
    return secretWord


# change letters of secretWord to _
def giveHint(secretWord):
    global number_words
    for i in range(len(secretWord)):
        number_words += "_"
    return number_words


# input a guessd letter and save it in an array
def GuessWord():
    global guessed_letter_list
    if guessed_letter_list != []:
        print("You have picked %s" % guessed_letter_list)
    guessed_word = input("Guess one charactor: ")
    if len(guessed_word) > 1:
        print("Choose only one letter!")
        GuessWord()
    else:
        if guessed_word in guessed_letter_list:
            print("You have already picked %s" % guessed_word)
            print("Choose other charactor")
            GuessWord()
        else:
            guessed_letter_list.append(guessed_word)
    return guessed_word


# compare letters of the secretWord and a guessed word
def CheckWord(secretWord, guessed_word):
    global number_words
    if guessed_word in secretWord:
        split_secretWord = list(secretWord)
        split_number_words = list(number_words)
        for i in range(len(split_secretWord)):
            if split_secretWord[i] == guessed_word:
                split_number_words[i] = split_secretWord[i]
            else:
                pass
        number_words = ''.join(split_number_words)
        print("Correct! " + number_words)
        return number_words
    else:
        print("Wrong... " + number_words)
        return False


# count the number of mistakes and check game clear or game over
def ClearOrGameOver(check_results, secretWord):
    global life
    if check_results == secretWord:
        print("Congratulation!!")
        pass
    elif check_results is False:
        life -= 1
        if life > 0:
            print("You can make mistake %s times" % life)
            Hangman(secretWord)
        else:
            print("Game Over. The SecretWord is %s" % secretWord)
            pass
    else:
        Hangman(secretWord)


# one process of hangman
def Hangman(secretWord):
    global number_words
    guessed_word = GuessWord()
    check_results = CheckWord(secretWord, guessed_word)
    ClearOrGameOver(check_results, secretWord)


# repeat hangman
def playGame():
    secretWord = loadWord()
    number_words = giveHint(secretWord)
    print(number_words)
    Hangman(secretWord)


# play game
playGame()
