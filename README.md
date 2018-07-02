# Python Basic

**This course is for:** Complete beginners in programming and people who know some basics but want to learn some tricks and more about standard libraries.

**This course is not for:** Experienced python programmers or anyone who knows about everything learnpython.org offers.

Before the actual course, I strongly recommend to try to get familiar with the language using those tutorials in links below or watching videos and trying out some things on your own.

# Videos
18/06/27 - [[Arch Classroom] Python for Beginners #1](https://www.youtube.com/watch?v=z3GJpjyCqyQ) (timestamps WIP, subtitles correction=0%)
18/07/04 - [[Arch Classroom] Python for Beginners #2]() (timestamps WIP, subtitles correction=0%)

# About the lecturer

Pulec is:
* Using Python for 6 years, last year professional with attending few lectures, rest is self tought and experience.
* Education: High School of Electronics (bad grades) && Unfinished Organic Agriculture
* Using Arch Linux for 6 years and working in Red Hat
* Likes: Open Source anything (Software, Games, Blueprints), Gardens inspired by Nature & wine

## Contents|Plan of education

1. Intro presentation; Crash Course through all basics of http://learnpython.org/ with few examples in ipython notebook
2. First useful program, having a problem, solving it, using the solution
3. Practice, Practice, Practice..tbd!
4. Time for a project of yours.
5. More theory, useful tips, delving deeper into topic X (Where X is whatever problem students will have)
6. Where to go next, final questions, summary
7.  tbd..packaging
8. tbd..sumary


## Install Python
* Arch : # pacman -S python3 ipython
* Linux && Windows : [Video tutorial](https://www.youtube.com/watch?v=YYXdXT2l-Gg&t=34s&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=1)
* OSX : [python-ugide-pt-br.readthedocs.io](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/)

## Prepare IPython Notebook

Ideal way to share code is via Jupyter Notebooks, the ipynb files in this repo are what we went/will go through in YouTube streams.

It can run code snippets or whole programs in organized form and allows to make nice documents with Markdown notes inside.

Making graphs and other things which requires some 'web magic' is easy in these notebooks compared to regular shell.

[Jupyter](https://wiki.archlinux.org/index.php/Jupyter)@archwiki:
> [Jupyter](http://jupyter.org/) is a project which produces browser-based interactive environments for programming, mathematics, and data science. It supports a number of languages via plugins ("kernels"), such as Python, Ruby, Haskell, R, Scala and Julia.
> Jupyter Notebook is the traditional and most stable application. [JupyterLab](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906) has a new interface and is more suitable for working with larger projects consisting of multiple files. JupyterLab is in beta as of February 2018.

### Sane way
On Arch just install jupyter and you can run jupyter notebook to start the server and browse ipynbs in this repo.

### Virtualenv way

Other way is virtualenv (Arch: extra/python-virtualenv) which will probably work on most systems and might be interesting to learn if you haven't done this before

Create one in any directory by running:

```
virtualenv edu
```

where edu is the folder which will be created. Activate it by running source edu/bin/activate and then do

```
pip install jupyter
```

which will install close to 40 packages, or you can do the same by running
```
pip install -r requirements.txt
```

Then run:
```
jupyter notebook
```

And open one of the files with ipynb extensions. 

## Start using Python:
Just dive in, you can read about it later
* Guided tutorial - [learnpython.org](http://learnpython.org/) - no installation needed, ipython in browser
* [repl.it/languages/python3](https://repl.it/languages/python3) - write code, run it, share it
* [pythonanywhere.com](https://www.pythonanywhere.com/try-ipython/) - ipython terminal online

## Read something:
Now when you have some idea how its used try reading something
* [Official tutorial](https://docs.python.org/3.6/tutorial/)
* [Myths about Python](https://www.paypal-engineering.com/2014/12/10/10-myths-of-enterprise-python/)
* [Picking an Interpreter The State of Python (3 & 2) and Cpython, Jython, etc...](http://docs.python-guide.org/en/latest/starting/which-python/)
* [Non-Programmer's Tutorial for Python 3](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3)

### Books:
* Dive Into Python 3
	* [eng](http://www.diveintopython3.net/)
	* [cz](http://diveintopython3.py.cz/index.html)
* [Porting from python2 to python3](http://python3porting.com/pdfs/SupportingPython3-screen-1.0-latest.pdf)
* [Test-Driven Development with Python](https://www.obeythetestinggoat.com/pages/book.html#toc)
* Lots of free books avaliable
	* [Directory of Python books - Junnplus/awesome-python-books](https://github.com/Junnplus/awesome-python-books)
	* [wiki.python.org](https://wiki.python.org/moin/PythonBooks)
	* [Books search at reddit.com/r/Python](https://www.reddit.com/r/Python/search?q=books&restrict_sr=1) 


## Watch Videos:
* Python Programming Beginner Tutorials - [19 videos around 20 minutes each](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)
* Any lecture from Raymond Hettinger - [currently 22 talks](https://www.youtube.com/watch?v=HTLu2DFOdTg&list=PLRVdut2KPAguz3xcd22i_o_onnmDKj3MA)

## Additional Interactive tutorials:
* [Bento.io - python/tutorials](https://bento.io/topic/python/tutorials)
* [Pythonroom.com](https://pythonroom.com/login/)
* [CodeAcademy.com](https://www.codecademy.com/learn/python)

## Practices

For practice try:

1. Try to write a script(program) where you declare 2 numbers to variables and it compares what is larger, what is smaller or if its equal.
Print out some message for each situation and try all different test cases (first number larger, first number lower, equal numbers)
2. More to come...

## Links
### Communities:
* [reddit.com/r/Python](https://www.reddit.com/r/Python)
* [reddit.com/r/learnpython](https://www.reddit.com/r/learnpython/)

Corey's beginners tutorial was recently posted on [reddit.com/r/learnprogramming/comments/6bxdut](https://www.reddit.com/r/learnprogramming/comments/6bxdut/python_for_beginners_complete_series/)

### Also visit:
* [pyvideo.org](http://pyvideo.org/) or search for pycon on youtube for interesting lectures

### Cheatsheets
* [Begginers Python Cheat Sheet](https://www.reddit.com/r/learnpython/comments/4y06nq/beginners_python_cheat_sheets_updated/)
* [ehmatthes.github.io](http://ehmatthes.github.io/pcc/cheatsheets/README.html)

### IPython and Jupyter Notebook
* [Ipython docs](http://ipython.readthedocs.io/en/stable/interactive/tutorial.html)
* [Jupyter notebook tips and tricks](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

### Deeper reading
* [Algorithms - Computer Science](http://interactivepython.org/runestone/static/pythonds/Introduction/toctree.html)

### Libraries overview
* [pythonpedia.com](https://pythonpedia.com/)
* [awesome-python](https://github.com/vinta/awesome-python)
* [Projects ideas](https://github.com/karan/Projects)

### Machine Learning video Tutorials
* [Udacity Introduction - Intro to Machine Learning (494 short videos)](https://www.youtube.com/watch?v=ICKBWIkfeJ8&list=PLAwxTw4SYaPkQXg8TkVdIvYv4HfLG7SiH)
* [Hello World - Machine Learning Recipes #1](https://www.youtube.com/watch?v=cKxRvEZd3Mw)

### Web
* [Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Electronics
* [czech article root.cz about circuits](https://www.root.cz/clanky/python-a-simulacia-elektronickych-obvodov/