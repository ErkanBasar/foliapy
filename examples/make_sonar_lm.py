#!/usr/bin/env python
#-*- coding:utf-8 -*-

#Create a language model based on SoNaR

import sys
from pynlpl.input.sonar import Corpus
from pynlpl.lm.lm import SimpleLanguageModel

#syntax: ./make_sonar_lm.py sonar_dir output_file n

outputfile = sys.argv[2]

try:
    n = int(sys.argv[3])
except:
    n = 3

lm = SimpleLanguageModel(n)

for doc in Corpus(sys.argv[1]):
    for sentence_id, sentence in doc:
        words = [ word for word, id, pos, lemma in sentence ]
        lm.append(words)
lm.save(outputfile)




