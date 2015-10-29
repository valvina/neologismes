# -*- coding: utf-8 -*-
import os
import unicodedata
import codecs

text_input = raw_input('Enter a file name:\n')
with open(text_input) as f:	
    text_input = f.read().split()
text_input = str(text_input)


"""
data="UTF-8 DATA"
udata=data.decode("utf-8")
asciidata=udata.encode("ascii","ignore")
print 'ok' """


def supprime_accent(text_input):
    accents = { 'a': ['à', 'ã', 'á', 'â'], 
                'e': ['é', 'è', 'ê', 'ë'],
                'i': ['î', 'ï'],
                'u': ['ù', 'ü', 'û'],
                'o': ['ô', 'ö'] }
    for (char, accented_chars) in accents.iteritems():
        for accented_char in accented_chars:
            text_input = text_input.replace(accented_char, char)
    return text_input
  
supprime_accent(text_input)
print 'done'

dict_angl_debut_mot = {'z': None}
dict_angl_milieu_mot = {'ght': None, 'oo': None, 'ee': None, 'ea': None, 'rat': None,  'ecti': None}
dict_angl_fin_mot = {'om': None, 'ing': None, 'ess': None, 'ff': None, 'ith': None, 'ty': None, 'ed': None, 'over': None, 'f': None, 'eve': None, 'fore': None, 'ng': None, 'th': None, 'our': None, 'ic': None, 'ly': None, 'or': None, 'er': None}

dict_neolog_debut_mot = {'z': None}
dict_neolog_milieu_mot = {}
dict_neolog_fin_mot = {'c': None, 'arde': None, 'f': None, 'o': None, 'ard': None, 'z': None, 'os': None}

dict_troncats = {'o': None, 'os': None, 'i': None, 'a': None}

dict_angl_text1 = {}
dict_angl_text2 = {}
dict_angl_text3 = {}
dict_angl_text4 = {}

dict_neolog_text1 = {}
dict_neolog_text2 = {}
dict_neolog_text3 = {}


dict_troncats_text1 = {}


text_input = raw_input('Enter a file name:\n')

def find_anglicismes(text_input):

	with open(text_input) as f:	
		for word in f.read().split():
			for x in dict_angl_debut_mot:
				if x in dict_angl_debut_mot and x == word[0]:
					dict_angl_text1.update({word: 1})
			for x in dict_angl_milieu_mot:
				if x in dict_angl_milieu_mot and x in word:
					dict_angl_text2.update({word: 2})
			for x in dict_angl_fin_mot:
				if x in dict_angl_fin_mot and x == word[-4:] or x == word[-3:]:
					dict_angl_text3.update({word: 3})
			for x in dict_angl_fin_mot:
				if x in dict_angl_fin_mot and x == word[-2:] or x == word[-1:]:
					dict_angl_text4.update({word: 4})


	print 'Anglicismes', '\n'
	print dict_angl_text1, '\n'
	print dict_angl_text2, '\n'
	print dict_angl_text3, '\n'
	print dict_angl_text4, '\n'
						

def find_neologismes(text_input):

	with open(text_input) as f:	
		for word in f.read().split():
			for x in dict_neolog_debut_mot:
				if x in dict_neolog_debut_mot and x == word[0]:
					dict_neolog_text1.update({word: 1})
			for x in dict_neolog_milieu_mot:
				if x in dict_neolog_milieu_mot and x in word:
					dict_neolog_text2.update({word: 2})
			for x in dict_neolog_fin_mot:
				if x in dict_neolog_fin_mot and x == word[-4:] or x == word[-3:] or x == word[-2:] or x == word[-1]:
					dict_neolog_text3.update({word: 3})


	print 'Neologismes', '\n'
	print dict_neolog_text1, '\n'
	print dict_neolog_text2, '\n'
	print dict_neolog_text3, '\n'


def find_troncats(text_input):

	with open(text_input) as f:	
		for word in f.read().split():
			for x in dict_troncats:
				if x in dict_troncats and x == word[-2:] or x == word[-1]:
					dict_troncats_text1.update({word: 1})


	print 'Troncats', '\n'
	print dict_troncats_text1, '\n'


find_anglicismes(text_input)
find_neologismes(text_input)
find_troncats(text_input)






