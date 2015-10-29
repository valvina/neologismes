# coding: utf8
import fileinput, unicodedata
import sys, re


text = open(sys.argv[1], "r")

dict_candidates = {}


for line in text:
        x = '<unknown>'
        words_in_line = line.split("\t")  # split lines in words
        if x in words_in_line[2]:
                try:
                        if dict_candidates[words_in_line[0]] in dict_candidates:
                                dict_candidates[words_in_line[0]]=dict_candidates[words_in_line[0]]+1
                except KeyError:
                        dict_candidates[words_in_line[0]]=1



with open("file_out.txt", "w") as sortie:
        for x in dict_candidates.keys(): 
                sortie.write("{}:{}\n".format(x,dict_candidates[x]))


text.close()
