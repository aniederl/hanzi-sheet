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


Using this Sheet on Windows
---------------------------

### Git ###
Install [Git for Windows][7] on your system.

#### Fetch this repository ####
* Open a **Git Bash** from your Start Menu
* Run
<pre>
git clone git@github.com:aniederl/hanzi-sheet.git
</pre>


### ConTeXt ###
Install [ConTeXt Standalone][1] for Windows:

* Extract **context-setup-mswin.zip** into your user directory
* Open cmd.exe and change into the extracted directory
	(e.g. **C:\Users\Hugo\context**)
* Run
<pre>
first-setup.bat --modules=all
</pre>

#### Add ConTeXt to the System Path ####
* Open the Properties window for **Computer** in your Start Menu (or your
	Desktop)
* Open extended system properties
* Go to **Advanced**
* Click on **Environment Variables** (on the bottom)
* In **System Variables** lookup the variable **Path**
* Click on **Edit**
* Go to the end of the variable value, enter a semicolon (**;**)
* Append the path to the context binary directory **tex\texmf-mswin\bin**, e.g.
<pre>
...SVN/bin;C:\Users\Hugo\context\tex\texmf-mswin\bin
</pre>

#### Run initial user setup for ConTeXt Mark IV ####
* Open a **Git Bash** from your Start Menu
* Run
<pre>
mtxrun  --generate
context --make
</pre>


#### Add Windows TrueType Fonts to ConTeXt ####
* Go the the **System Variables** as before
* Create a new System Variable named **OSFONTDIR**
* Set its value to
<pre>
c:/windows/fonts/
</pre>
* Note that normal slashes (**/**) are used here in contrast to the backslashes
	(**\\**) before
* Lookup the font **STKaiti** on the Internet and download it
* Right-Click on the font file and select **Install**
* Open a **Git Bash** from your Start Menu
* Run
<pre>
mtxrun --script fonts --reload
</pre>


### Python 3 ###
Install [Python version 3][8] for your Windows version.
Add the Python binary to your **Path** variable:

* Go to the System Environment Variable **Path** as before in section *ConTeXt*
* Go to the end of the variable value, enter a semicolon (**;**)
* Append the path to the python directory **C:\Python32**, e.g.
<pre>
...\texmf-mswin\bin;C:\Python32
</pre>


### Use this Sheet ###
* Open a **Git Bash** from your Start Menu
* Change directory to this repository
<pre>
cd hanzi-sheet/
</pre>
* Generate the sheet PDF with this command:
<pre>
context hanzi-sheet.tex
</pre>
* Open **hanzi-sheet.pdf** in Windows Explorer


   [1]: http://wiki.contextgarden.net/ConTeXt_Standalone "ConTeXt"
   [2]: http://wiki.contextgarden.net/Running_Mark_IV    "Running Mark IV"
   [3]: http://wiki.contextgarden.net/Fonts_in_LuaTeX    "Fonts in LuaTeX"
   [4]: http://ankisrs.net/  "Anki"
   [5]: http://wiki.contextgarden.net/Fonts_in_LuaTeX#Installing_simplefonts "Installing simplefonts"
   [6]: http://wiki.contextgarden.net/write18 "Enabling external programs"
   [7]: http://code.google.com/p/msysgit/ "Git for Windows"
   [8]: http://www.python.org/getit/ "Download Python"

