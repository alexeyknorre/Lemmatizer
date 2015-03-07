# -*- coding: utf-8 -*-
"""
Simple script for lemmatization of Russian text.
Alexey Knorre
a.v.knorre@gmail.com
07.03.2015
"""

import os
import pymorphy2
import re
import chardet

#Collecting files
print "Indexing text files..."
current_dir = os.path.dirname(os.path.abspath(__file__))

files = [ f for f in os.listdir(current_dir) if f.lower().endswith('.txt') and os.path.isfile(os.path.join(current_dir,f)) ]


#Creating dir for storing lemmatized files
if not os.path.exists(current_dir+"\\lemmatized"):
    os.makedirs(current_dir+"\\lemmatized")

#Cycle for reading files

for f in files:
    with open(current_dir+"\\"+f) as text:
        text = text.read()
    print "Working with file "+f         
#Detecting codepage, recoding, cleaning, lemmatizing
    codepage = chardet.detect(text)['encoding']
    text = text.decode(codepage)
    text = " ".join(word.lower() for word in text.split()) #lowercasing and removing short words 
    text = re.sub('\-\s\r\n\s{1,}|\-\s\r\n|\r\n', '', text) #deleting newlines and line-breaks
    text = re.sub('[.,:;%©?*,!@#$%^&()\d]|[+=]|[[]|[]]|[/]|"|\s{2,}|-', ' ', text) #deleting symbols  
    text = " ".join(pymorphy2.MorphAnalyzer().parse(unicode(word))[0].normal_form for word in text.split())
    text = text.encode("utf-8")

    
    path,file_name=os.path.split(f)
    with open(current_dir+"\\lemmatized\\"+f,'w') as f:
        f.write(text)
print "Done."

