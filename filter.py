#!/usr/bin/python3
#
# Filter script for filtering Anki text exports for entries containing only one
# symbol and writing those symbols newline-separated into another file
# Note that the Anki export should have the symbols in the first column
#
# This script needs Python version 3 or higher
#

import sys

from optparse import OptionParser

usage  = "Usage: %prog input-file output-file"
parser = OptionParser(usage)

parser.add_option("-t", "--tex", action="store_true", dest="output_tex",
    default=False)
parser.add_option("-p", "--reading", action="store_true", dest="add_reading",
    default=False)

(options, args) = parser.parse_args()

if len(args) < 2:
  parser.error("incorrect number of arguments")

in_file  = args[0]
out_file = args[1]


import re
delim1 = '\t+|<br\s*/>'
delim  = '(?:\t+|<br\s*/>|$)+'
text   = '([\S ]+?)'
symbol_re = re.compile(r'^(\w)'  + delim + text + delim + text + delim, re.UNICODE)
word_re   = re.compile(r'^(\w+)' + delim + text + delim + text + delim, re.UNICODE)

hanzi = set()
words = set()
word_list = list()
readings        = dict()
translations    = dict()
processed_words = set()


try:
  in_f  = open(in_file, 'r', encoding='utf-8')
  out_f = open(out_file, 'w', encoding='utf-8')
except IOError as err:
  print(err)
  sys.exit(err.errno)


def printline(word, symbol, reading, translation):
  output = ''

  if options.output_tex:
    if options.add_reading:
      output = '\\linedesc[' + word + '][' + symbol + \
          '][' + reading + '][' + translation + ']'
    else:
      output = '\\line{' + symbol + '}'
  else:
    output = symbol

  output += '\n'
  out_f.write(output)


for line in in_f:
  line   = re.sub('&quot;', '\'', line)
  match  = word_re.match(line)

  if match:
    word = match.group(1)
    reading = match.group(2)
    reading = re.sub('<br\s*/>', '', reading)
    translation = match.group(3)

    word_list.append(word)
    words.add(word)
    readings[word]     = reading
    translations[word] = translation


print_words = list()
added_words = set()
added_syms  = set()
for phrase in word_list:
  #print("phrase: " + phrase)
  for step in range(1, len(phrase)+1):
    for i in range(0, len(phrase)):
      j    = i + step
      word = phrase[i:j]

      #print("look: " + word)
      if word in words and not word in added_words:
        new = 0
        for sym in word:
          if not sym in added_syms:
            new += 1

        if new > 0:
          #print("append: " + word + " - " + translations[word])
          print_words.append(word)
          added_words.add(word)

          for sym in word:
            added_syms.add(sym)


for word in print_words:
  for symbol in word:
    if symbol in hanzi:
      #print(symbol + " already done")
      continue

    hanzi.add(symbol)
    printline(word, symbol, readings[word], translations[word])

