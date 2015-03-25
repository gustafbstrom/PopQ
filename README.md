PopQ
====
A terminal pop-question memory test

How to run
==========
Call `python main.py` directly or add the command to your bashrc or whatever shell start up scrip you are using.

How to add questions?
=====================
Create a new file in the `questions` subdirectory and write a python dictionary on the form:

```
foo = {
    ("My question", "answer")
}
```

The name of the file becomes the category.

