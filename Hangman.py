import random
random.seed(1)


guessed_word_list = []
life = 6
number_words = ""


def loadWord():
    f = open('hangman_words.txt', 'r')
    wordsList = f.readlines()
    f.close()

    wordsList = wordsList[0].split(' ')
    secretWord = random.choice(wordsList)
    return secretWord


def giveHint(secretWord):
    global number_words
    for i in range(len(secretWord)):
        number_words += "_"
    return number_words


def GuessWord():
    global guessed_word_list
    if guessed_word_list != []:
        print("You have picked %s" % guessed_word_list)
    guessed_word = input("Guess one charactor: ")
    if guessed_word in guessed_word_list:
        print("You have already picked %s" % guessed_word)
        print("Choose other charactor")
        GuessWord()
    else:
        guessed_word_list.append(guessed_word)
    return guessed_word


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
        print(number_words)
        return number_words
    else:
        return False


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
            print("Game Over")
            pass
    else:
        Hangman(secretWord)


def Hangman(secretWord):
    global number_words
    guessed_word = GuessWord()
    check_results = CheckWord(secretWord, guessed_word)
    ClearOrGameOver(check_results, secretWord)


secretWord = loadWord()
print(secretWord)
number_words = giveHint(secretWord)
Hangman(secretWord)
