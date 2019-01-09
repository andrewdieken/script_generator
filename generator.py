import pandas as pd
import numpy as np
import os
import string
import re
import random

# v is the number of unique words
# first pass, record all unique words. then we know how many unique words we have
# second pass do all other stuff

# keep track of all unique words and how many times they appear

#Steps
## Generate starting word = current state
## Need to predict next state based on current state



def createWordList():
    uniqueWordList= []
    wordDict = {}

    directory = os.fsencode(".")
    for file in os.listdir(directory):
        try:
            filename = os.fsdecode(file)
            if filename == 'generator.py' or filename == 'the-lion-king.txt':
                continue
            else:
                # loop over each for and put into dictionary
                currentScript = open(filename, "r")
                for sentence in currentScript:
                    sentence = sentence.split(' ')
                    for word in sentence:
                        word = re.sub("[^a-zA-Z']", '', word)
                        word = word.rstrip()
                        if word not in uniqueWordList:
                            uniqueWordList.append(word)
                            wordDict[word] = 1
                        else:
                            wordDict[word] += 1
            break
        except UnicodeDecodeError:
            print("File couldn't be read because of encoding error")


    return uniqueWordList, wordDict

#=======================================================

#=======================================================

def generateStartingWord(list):
    ranNum = random.randint(1, (len(list) + 1))
    word = list[ranNum]
    return word

#=======================================================
 # matrix 1 = track current and next words
 # matrix 2 = transitionMatrix to track probabilities

def generateWordMatrix(wordsList):
    #go through the files one by one
    #have 2 pointers: 1 -> current word, 2-> next word
    curr = ''
    next = ''
    x = np.zeros((4742,4742))
    #loop through files
    directory = os.fsencode(".")
    for file in os.listdir(directory):
        try:
            filename = os.fsdecode(file)
            if filename == 'generator.py' or filename == 'the-lion-king.txt':
                continue
            else:
                # loop over each for and put into dictionary
                currentScript = open(filename, "r")
                for sentence in currentScript:
                    if len(sentence) == 0:
                        continue
                    sentence = sentence.split(' ')
                    for word in sentence:
                        word = re.sub("[^a-zA-Z']", '', word)
                        word = word.rstrip()

            break
        except UnicodeDecodeError:
            print("File couldn't be read because of encoding error")







if __name__ == "__main__":
    uniqueWordList, wordDict = createWordList()
    #wordDict = createUniqueWordDict()
    totalWords = len(uniqueWordList)

    startingWord = generateStartingWord(uniqueWordList)

    #print(wordDict)
    print('Number of unique words: ', totalWords)
    print(startingWord)


    generateWordMatrix(uniqueWordList)
