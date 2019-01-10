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
    #uniqueWordList= []
    wordDict = {}
    i = 0

    directory = os.fsencode(".")
    for file in os.listdir(directory):
        try:
            filename = os.fsdecode(file)
            if filename == 'generator.py' or filename == 'the-lion-king.txt' or filename == '.git':
                continue
            else:
                # loop over each for and put into dictionary
                print(filename)
                currentScript = open(filename, "r")
                for sentence in currentScript:
                    sentence = sentence.split(' ')
                    for word in sentence:
                        word = re.sub("[^a-zA-Z']", '', word)
                        word = word.rstrip()
                        if word not in wordDict:
                            #uniqueWordList.append(word)
                            wordDict[word] = i
                            i += 1
            #break
        except UnicodeDecodeError:
            print("File couldn't be read because of encoding error")


    return wordDict

#=======================================================

#=======================================================

def generateStartingWord(list):
    ranNum = random.randint(1, (len(list) + 1))
    word = list[ranNum]
    return word

#=======================================================
 # matrix 1 = track current and next words
 # matrix 2 = transitionMatrix to track probabilities

def generateWordMatrix(wordsDict):
    #go through the files one by one
    #have 2 pointers: 1 -> current word, 2-> next word
    curr = ''
    next = ''
    size = len(wordsDict)
    x = np.zeros((size,size))
    #loop through files
    directory = os.fsencode(".")
    for file in os.listdir(directory):
        temp_script = []
        try:
            filename = os.fsdecode(file)
            if filename == 'generator.py' or filename == 'the-lion-king.txt' or filename == '.git':
                continue
            else:
                # loop over each for and put into dictionary
                currentScript = open(filename, "r")
                for sentence in currentScript:
                    if len(sentence) == 0:
                        continue
                    sentence = sentence.split(' ')
                    for word in sentence:
                        if word == '' or word == '\\n':
                            continue
                        else:
                            word = re.sub("[^a-zA-Z']", '', word)
                            word = word.rstrip()
                            if word != '':
                                temp_script.append(word)

            for i in range(len(temp_script)):
                if i < len(temp_script)-1:
                    curr = temp_script[i]
                    next = temp_script[i+1]
                    #print('current word: {} | next word: {}'.format(curr, next))
                    # Get indexs of words
                    curr_index = wordDict[curr]
                    next_index = wordDict[next]
                    #update matrix
                    x[curr_index][next_index] += 1

            #break
        except UnicodeDecodeError:
            print("File couldn't be read because of encoding error")



    return x




if __name__ == "__main__":
    wordDict = createWordList()
    #print(wordDict)
    #wordDict = createUniqueWordDict()
    totalWords = len(wordDict)

    #startingWord = generateStartingWord(uniqueWordList)

    #print(wordDict)
    print('Number of unique words: ', totalWords)


    seen_matrix = generateWordMatrix(wordDict)
    print(seen_matrix)
