# ~~~~~~COMPARISON OF TWO DOCUMENTS THROUGH HIS DISTANCE~~~~~~
#
#
#
# Made by Pau Sabates Campos

import sys
import math
import Tkinter
from tkSimpleDialog import *
import tkMessageBox

degr = 57.2957795  # convert rad to degrees
same_words = 0


def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.readlines()
    except IOError:
        print "Error opening or reading input file: ", filename
        tkMessageBox.showinfo("Error :(", "Error opening or reading input file :(")
        # sys.exit()


def get_words_from_line_list(L):
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list.extend(words_in_line)
    return word_list


def get_words_from_string(line):
    """
    word_list = []
    w=line.split(" ")
    for i in range(len(w)):
        word_list.append(stemWord(w[i]))
    return word_list

    """
    extension = 0
    word_list = []
    character_list = []
    for c in line:
        if extension:
            if c == " ":
                extension = 0
            elif c == "t":
                word_list.append("not")
            elif c == "v":
                word_list.append("have")
            elif c == "r":
                word_list.append("are")
            continue

        if c.isalnum():
            character_list.append(c)
        elif len(character_list) > 0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
            if c != " ":
                extension = 1
    if len(character_list) > 0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
    return word_list


def count_frequency(word_list):
    D = {}
    for paraula in word_list:
        if paraula in D:
            D[paraula] = D[paraula] + 1
        else:
            D[paraula] = 1
    return D.items()


def word_frequencies_for_file(filename, num):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)

    # print "File",filename,":",
    # print len(line_list),"lines,",
    # print len(word_list),"words,",
    # print len(freq_mapping),"distinct words"

    text = Label(root, text="File: %s" % filename, bg='#DBAEA4')
    # text.grid(row=num, column=0, padx=70)
    # text.configure(background='#DBAEA4')
    text.place(relx=0.0, rely=0.36 + num)
    text = Label(root, text="lines: %s" % len(line_list), bg='#DBAEA4')
    # text.grid(row=num, column=1)
    # text.configure(background='#DBAEA4')
    text.place(relx=0.20, rely=0.36 + num)
    text = Label(root, text="words: %s" % len(word_list), bg='#DBAEA4')
    # text.grid(row=num, column=2)
    # text.configure(background='#DBAEA4')
    text.place(relx=0.28, rely=0.36 + num)
    text = Label(root, text="distinct words: %s" % len(freq_mapping), bg='#DBAEA4')
    # text.grid(row=num, column=3)
    # text.configure(background='#DBAEA4')
    text.place(relx=0.38, rely=0.36 + num)
    return freq_mapping


def inner_product(L1, L2):
    sum = 0.0
    global same_words
    same_words = 0
    for word1, count1 in L1:
        for word2, count2 in L2:
            if word1 == word2:
                sum += count1 * count2
                same_words += 1
    return sum


def vector_angle(L1, L2):
    numerator = inner_product(L1, L2)
    denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
    return math.acos(numerator / denominator)


def Fichero1():
    x1 = Entry.get(x)
    sorted_word_list_1 = word_frequencies_for_file(x1, 0)
    fitx.anade1(sorted_word_list_1)


def Fichero2():
    x2 = Entry.get(y)
    sorted_word_list_2 = word_frequencies_for_file(x2, 0.1)
    fitx.anade2(sorted_word_list_2)


class general():
    def __init__(self, var1="x", var2="x"):
        self.vari1 = var1
        self.vari2 = var2
        self.distance = 1

    def anade1(self, var1):
        self.vari1 = var1

    def anade2(self, var2):
        self.vari2 = var2

    def distansia(self):
        self.distance = vector_angle(self.vari1, self.vari2)
        self.distance = self.distance * degr
        text = Label(root, text="The distance between the documents is: %f" % self.distance, bg='#758AE3',
                     font="-weight bold")
        text.place(relx=0.3, rely=0.72)
        text = Label(root, text="The number of words in common are: %i" % same_words, bg='#758AE3', font="-weight bold")
        text.place(relx=0.3, rely=0.8)



        # percentatge=(math.sin(self.distance)*100)
        # if percentatge == 0.0:
        # percentatge =100
        # text = Label(root, text="The documents are %0.2f equals"%percentatge)
        # text.grid(row=6, column=1)


if __name__ == "__main__":
