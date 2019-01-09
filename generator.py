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


def createWordList():
    uniqueWordList= []

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
            break;
        except UnicodeDecodeError:
            print("File couldn't be read because of encoding error")

    return uniqueWordList

#=======================================================

def createUniqueWordDict():
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
                        if word not in wordDict:
                            wordDict[word] = 1
                        else:
                            wordDict[word] += 1
            break;
        except UnicodeDecodeError:
            print("File couldn't be read because of encoding error")

    return wordDict

#=======================================================

def generateStartingWord(list):
    ranNum = random.randint(1, 4742)
    word = list[ranNum]

    return word




# #print(uniqueWordList)
# print(wordDict)
# print('total number of unique words: ', len(uniqueWordList))
#
# randomNum = random.randint(1, 4742)
# print('start word: ', uniqueWordList[randomNum])



if __name__ == '__main__':
    uniqueWordList = createWordList()
    wordDict = createUniqueWordDict()
    totalWords = len(uniqueWordList)

    startingWord = generateStartingWord(uniqueWordList)

    print(wordDict)
    print('Number of unique words: ', totalWords)
    print(startingWord)
