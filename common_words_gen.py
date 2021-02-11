import os
from pathlib2 import Path
import random

def generate_n_common_words(n):
    #open file and read each line into a list
    word_list = open('wordlist.10000.txt', 'r').readlines()

    #chose five random words.
    list_length = len(word_list)
    answer = ""
    for i in range(0,n):
        j = random.randint(0, list_length)
        if (i == 0):
            answer = word_list[j].strip()
        else:
            answer = "".join([answer, '_{}'.format(word_list[j]).strip()])
    return answer

print(generate_n_common_words(4))