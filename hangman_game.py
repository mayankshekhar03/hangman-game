# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    a = set([i for i in secretWord])
    j = 0
    for i in a:
        if i in lettersGuessed:
            j += 1
    if j == len(a):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed = []
    for l in range(len(secretWord)):
        guessed.append('_')
    for i in lettersGuessed:
        for j in range(len(secretWord)):
                if i == secretWord[j] and guessed[j] == '_':
                    guessed[j] = secretWord[j]
    return str(''.join(guessed))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    remain = [i for i in string.ascii_lowercase]
    for j in lettersGuessed:
        for k in remain:
            if j == k:
                remain.remove(k)
    return ''.join(remain)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alpha = string.ascii_lowercase
    guesses = 8
    print('Welcome to the game, Hangman')
    print('I am thinking of a word which is ' + str(len(secretWord)) + ' letters long.')
    bool = False
    lettersGuessed = []
    while (not bool) and (guesses > 0):
        print('-------------')
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + alpha)
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        currentGuess = str(getGuessedWord(secretWord, lettersGuessed))
        if guess in alpha:
            lettersGuessed.append(guess)
            alpha = getAvailableLetters(lettersGuessed)
            if guess in secretWord:
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                bool = isWordGuessed(secretWord, lettersGuessed)
            else:
                guesses -= 1
                print('Oops! That letter is not in my word: ' + currentGuess)
        else:
            print("Oops! You've already guessed that letter: " + currentGuess)
    
    if bool == True:
        print('-------------')
        print('Congratulations, you won!')
    else:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was ' + str(secretWord))
            
                
            
        
        
    # When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
