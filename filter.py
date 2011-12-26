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

(options, args) = parser.parse_args()

if len(args) < 2:
  parser.error("incorrect number of arguments")

in_file  = args[0]
out_file = args[1]


import re
symbol_re = re.compile(r'^(\w)\s+', re.UNICODE)


try:
  in_f  = open(in_file, 'r')
except IOError as err:
  print(err)
  sys.exit(err.errno)

out_f = open(out_file, 'w')
for line in in_f:
  symbol = symbol_re.match(line)
  if symbol:
    out_f.write(symbol.group(1) + '\n')


