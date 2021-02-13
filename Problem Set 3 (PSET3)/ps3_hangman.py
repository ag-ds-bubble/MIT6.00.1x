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
    _a = set(list(secretWord))
    _b = set(lettersGuessed)
    _c = _a.difference(_b)==set()
    return _c



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word =''
    for eletter in secretWord:
      if eletter in lettersGuessed:
        guessed_word+=eletter
      else:
        guessed_word+='_'
    return guessed_word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_letters = set(list('abcdefghijklmnopqrstuvwxyz'))
    remaining_letters = all_letters.difference(set(lettersGuessed))
    remaining_letters = sorted(remaining_letters)
    remaining_letters = "".join(list(remaining_letters))
    return remaining_letters    

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
    guesses_left = 8
    _guessed_word = ''
    _guessed_letters = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is',len(secretWord),'letters long.')
    while guesses_left>0:
      _available_letters = getAvailableLetters(_guessed_letters)
      print('-------------')
      print('You have',guesses_left,'guesses left.')
      print('Available letters: ', _available_letters)
      _guessed_letter = input("Please guess a letter:")
      _guessed_word = getGuessedWord(secretWord, _guessed_letters)
        
      if _guessed_letter in _guessed_letters:
        print("Oops! You've already guessed that letter:",_guessed_word)
      elif _guessed_letter in secretWord:
        _guessed_letters.append(_guessed_letter)
        _guessed_word = getGuessedWord(secretWord, _guessed_letters)
        print('Good guess:',_guessed_word)
      else:
        _guessed_letters.append(_guessed_letter)
        _guessed_word = getGuessedWord(secretWord, _guessed_letters)
        print('Oops! That letter is not in my word:',_guessed_word)
        guesses_left-=1

      if '_' not in _guessed_word:
        print('-------------')
        print('Congratulations, you won!')
        break

    if '_' in _guessed_word:
      print('-------------')
      print('Sorry, you ran out of guesses. The word was',secretWord,'.')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
