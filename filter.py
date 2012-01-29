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
parser.add_option("-p", "--pinyin", action="store_true", dest="add_pinyin",
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
symbol_re = re.compile(r'^(\w)'    + delim + text + delim + text + delim, re.UNICODE)
word_re   = re.compile(r'^(\w\w+)' + delim + text + delim + text + delim, re.UNICODE)

hanzi = set()


try:
  in_f  = open(in_file, 'r', encoding='utf-8')
except IOError as err:
  print(err)
  sys.exit(err.errno)


def printline(line, regex, out):
  match  = regex.match(line)
  output = ''

  if match:
    word = match.group(1)

    for symbol in word:
      if symbol in hanzi:
        continue

      hanzi.add(symbol)

      if options.output_tex:
        if options.add_pinyin:
          pinyin = match.group(2)
          pinyin = re.sub('<br\s*/>', '', pinyin)
          desc   = match.group(3)
          output = '\\linedesc[' + word + '][' + symbol + '][' + pinyin + '][' + desc + ']'
        else:
          output = '\\line{' + symbol + '}'
      else:
        output = symbol

      output += '\n'
      out.write(output)


out_f = open(out_file, 'w', encoding='utf-8')
for line in in_f:
  line = re.sub('&quot;', '\'', line)
  printline(line, symbol_re, out_f)

in_f.seek(0)
for line in in_f:
  line = re.sub('&quot;', '\'', line)
  printline(line, word_re, out_f)

