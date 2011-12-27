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
Remember that you have to set the environment variable **OSFONTDIR** according to
the paths where your fonts can be found. This can be done on Windows somewhere
on the 'My Computer' settings, if I remember correctly.

For the ConTeXt Standalone version (on Windows) the packages **simplefonts** and
**filter** need to be [installed][5].

Python version 3 is required for the filter which generates the content from an
Anki export. The default configuration of ConTeXt has to be [changed][6] to allow
running external programs.


Usage
-----
To generate practice sheets you can provide your own [Anki][4]
export file and point to it by exchanging the file name used at the bottom of
the TeX document.

The export file is required to have lines with fields separated by either a
tabulator character or one or more *&lt;br /&gt;* tags in this form:

    你	nǐ<br /><br /><br />du


Compile the document using this commandline:

    context hanzi-sheet.tex


### Using Lua ###
You can use the LuaTeX function **userdata.readhanzi()** for generating simple
practice sheets using a source file with one character per line.

An example source file is included in this repository: **hanzi.txt**.

The python script **filter.py** can be used to generate such a newline-separated
symbol file from an Anki export:

    python filter.py zhongwen.txt hanzi.txt


   [1]: http://wiki.contextgarden.net/ConTeXt_Standalone "ConTeXt"
   [2]: http://wiki.contextgarden.net/Running_Mark_IV    "Running Mark IV"
   [3]: http://wiki.contextgarden.net/Fonts_in_LuaTeX    "Fonts in LuaTeX"
   [4]: http://ankisrs.net/  "Anki"
   [5]: http://wiki.contextgarden.net/Fonts_in_LuaTeX#Installing_simplefonts "Installing simplefonts"
   [6]: http://wiki.contextgarden.net/write18 "Enabling external programs"

