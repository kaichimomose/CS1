import requests
from bs4 import BeautifulSoup
from collections import Counter
# from string import punctuation
import random
random.seed(2)


guessed_letter_list = []
life = 6
count_correct = 0
number_words = ""


# pick a word up
def loadWord():
    quote_page = "https://www.makeschool.com/product-college/students"
    page = requests.get(quote_page)
    soup = BeautifulSoup(page.content, "html.parser")
    text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))

    c = Counter((x.lower() for y in text for x in y.split() if x.isalpha() is True))
    wordsList = [x for x in c if c.get(x) > 0]

    secret_word = random.choice(wordsList)
    return secret_word


# change letters of secretWord to _
def giveHint(secret_word):
    global number_words
    for i in range(len(secret_word)):
        number_words += "_"
    return number_words


# input a guessd letter and save it in an array
def guessLetter():
    global guessed_letter_list
    if guessed_letter_list != []:
        print("You have picked %s" % guessed_letter_list)
    guessed_letter = input("Guess one charactor: ")
    if len(guessed_letter) > 1:
        print("Choose only one letter!")
        guessLetter()
    elif guessed_letter.isalpha() is False:
        print("You did not pick a letter.")
        guessLetter()
    elif guessed_letter in guessed_letter_list:
        print("You have already picked %s" % guessed_letter)
        print("Choose other charactor")
        guessLetter()
    else:
        guessed_letter_list.append(guessed_letter)
    return guessed_letter


# compare letters of the secretWord and a guessed word
def checkWord(secret_word, guessed_letter):
    global number_words
    global count_correct
    guessed_letter = guessed_letter.lower()
    if guessed_letter in secret_word:
        split_secret_word = list(secret_word)
        split_number_words = list(number_words)
        for i in range(len(split_secret_word)):
            if split_secret_word[i] == guessed_letter:
                split_number_words[i] = split_secret_word[i]
                count_correct += 1
            else:
                pass
        number_words = ''.join(split_number_words)
        print("Correct! " + number_words)
        return True
    else:
        print("Wrong... " + number_words)
        return False


# count the number of mistakes and check game clear or game over
def clearOrGameOver(check_results, secret_word):
    global life
    global number_words
    if check_results is False:
        life -= 1
        if life > 0:
            print("You can make mistake %s times." % life)
            hangman(secret_word)
        else:
            print("Game Over. The SecretWord is %s." % secret_word)
            pass
    else:
        if number_words == secret_word:
            print("Congratulation!! The SecretWord is %s!" % secret_word)
            pass
        else:
            guessWord(secret_word)


# be able to guess full secretWord if user corrects more than half of letters of secretWord
def guessWord(secret_word):
    global count_correct
    if count_correct >= len(secret_word)/2:
        guess_word = input("What is the secret word: ")
        if guess_word == secret_word:
            print("Congratulation!! The SecretWord is %s!" % secret_word)
            pass
        else:
            print("Wrong...")
            hangman(secret_word)
    else:
        hangman(secret_word)


# one process of hangman
def hangman(secret_word):
    global number_words
    guessed_letter = guessLetter()
    check_results = checkWord(secret_word, guessed_letter)
    clearOrGameOver(check_results, secret_word)


# repeat hangman
def playGame():
    secret_word = loadWord()
    number_words = giveHint(secret_word)
    print(number_words)
    hangman(secret_word)


# play game
playGame()
