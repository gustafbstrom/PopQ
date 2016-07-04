PopQ
====
A terminal pop-question memory test. 

Tested with Python 2.7 and 3.5.1

How to run
==========
Call `main.py` directly from the terminal or add a call to your bashrc or whatever shell start up scrip you are using.

Example
```
python main.py -q ~/questions/world_capitols.py ~/questions/latin_animal_family_names.py
```

PopQ accepts the following command-line options:
```
usage: main.py [-h] -q QUESTION_FILES [QUESTION_FILES ...] [-r RESOURCE_FILE]

A terminal pop-question memory test

optional arguments:
  -h, --help            show this help message and exit
  -q QUESTION_FILES [QUESTION_FILES ...], --question_files QUESTION_FILES [QUESTION_FILES ...]
  -r RESOURCE_FILE, --resource_file RESOURCE_FILE
```

How to add questions?
=====================
Create a new file and write a python dictionary on the form:

```
#category.txt
[
    ("My question", "answer")
]
```

The name of the file becomes the category.

