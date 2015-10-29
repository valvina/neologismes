# coding: utf8
# this program takes as argument a treetagger output file, retrive unknown words, save them into
# a dictionary and print them
## to be done : categorize the unknwon
## actuellement on n'enregistre les mots avec majuscule que s'ils existent aussi en minuscule!

import os, sys, re
import unicodedata as ud

latin_letters= {}

def is_latin(uchr):
    try: return latin_letters[uchr]
    except KeyError:
         return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))

def only_roman_chars(unistr):
    return all(is_latin(uchr)
           for uchr in unistr
           if uchr.isalpha()) # isalpha suggested by John Machin


## initialisation dict mot inconnu candidats

unkwown = {} # pour les mots inconnus en minuscule (ie ne commencant pas par majuscule)
unkwown2 = {}# pour les mots commencant par une majuscule

# lecture d'un fichier ligne à ligne
try:
	file = open('frout1.txt', 'r') #open(sys.argv[1], "r")
	file2 = open('fr_out.txt', 'w')#open(sys.argv[1]+".out.txt", "w")
	#print file, type(file)
except:
	print 'File cannot be opened : Please check if the file given as argument exists : ', file
	exit()
for line in file: ## lecture fichier ligne à ligne
	cpts = line.split("\t") # decoupage ligne en trois champs : mot tab pos tab lemme (format treetagger)
	if only_roman_chars(cpts[2].decode('utf8')):# fonction pour slt caracteres romans
		if re.search(r"unknown", cpts[2]): # on trouve un lemme unknown => candidats mots inconnus
			if cpts[0].decode('utf8').istitle() or cpts[0].decode('utf8').isupper(): ## reperage mot capitalise (title case) ou upper
				if cpts[0].strip() in unkwown:
					unkwown2[cpts[0].strip().lower()]=unkwown[cpts[0].strip().lower()]+1
				else:
					unkwown2[cpts[0].strip().lower()]=1
			else:
				if cpts[0].strip() in unkwown:
					unkwown[cpts[0].strip()]=unkwown[cpts[0].strip()]+1
				else:
					unkwown[cpts[0].strip()]=1

file.close()

# comparaison unknwown2 avec unknown on ne conserve que ceux qui existent en minuscule
nb_common=0
for word, freq in unkwown2.iteritems():
	if word in unkwown:
		unkwown[word]=unkwown[word]+1
		nb_common+=1

### ecriture resultat dans fichier out
file2.write("{} mots inconnus en majuscule\n".format(len(unkwown2) - nb_common))
file2.write("{} mots inconnus en minuscule\n".format(len(unkwown)))
for word, freq in unkwown.iteritems():
    file2.write( "{}\t{}\n".format(word, freq))
file2.close()
