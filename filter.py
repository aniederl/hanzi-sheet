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
symbol_re = re.compile(r'^(\w)' + delim + text + delim + text + delim, re.UNICODE)


try:
  in_f  = open(in_file, 'r')
except IOError as err:
  print(err)
  sys.exit(err.errno)

out_f = open(out_file, 'w')
for line in in_f:
  line = re.sub('&quot;', '\'', line)
  match = symbol_re.match(line)
  if match:
    symbol = match.group(1)
    output = ''
    if options.output_tex:
      if options.add_pinyin:
        pinyin = match.group(2)
        pinyin = re.sub('<br\s*/>', '', pinyin)
        desc   = match.group(3)
        output = '\\linedesc{' + symbol + '}{' + pinyin + '}{' + desc + '}'
      else:
        output = '\\line{' + symbol + '}'
    else:
      output = symbol

    output += '\n'
    #print(output)
    out_f.write(output)


