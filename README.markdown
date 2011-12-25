Hanzi Practice Sheet
====================

Requirements
------------
This practice sheet is a TeX document for the ConTeXt Mark IV typesetting
engine.

In order to compile it to a PDF file you need to have a
[ConTeXt][1] installation and to use it in [Mark IV][2] which is
still beta and therefore needs to be used explicitly.

For correct representation of the Chinese Hanzi you will also need to install a
suitable TrueType font containing these characters.
The example font used by default in this sheet is STKaiti which could be
acquired using a web search engine if you have not installed it in your system.

Font [installation][3] can be done by using the command line interface.
Remember that you have to set the environment variable OSFONTDIR according to
the paths where your fonts can be found. This can be done on Windows somewhere
on the 'My Computer' settings, if I remember correctly.


Usage
-----
To use this practice sheet you can provide your own [Anki][4]
export file and point to it by exchanging the file name used in the bottom of
the TeX document.

An export example is included in this repository in the file *zhongwen.txt*.

Compile the document using this commandline:
```
context hanzi-sheet.tex
```


   [1]: http://wiki.contextgarden.net/ConTeXt_Standalone "ConTeXt"
   [2]: http://wiki.contextgarden.net/Running_Mark_IV    "Running Mark IV"
   [3]: http://wiki.contextgarden.net/Fonts_in_LuaTeX    "Fonts in LuaTeX"
   [4]: http://ankisrs.net/  "Anki"

