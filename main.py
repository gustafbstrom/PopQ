#!/usr/bin/env python

import sys
import os
import time
import random
import tempfile




if __name__ == "__main__":


    # ============================
    # Traverse and load the input file list
    # ========================

    Questions = []

    for filepath in sys.argv[1:]:
        with open(filepath) as fp:
            print "Opening: ",filepath
            content = eval( fp.read() )
            print "Loaded :",len(content)," questions"
            Questions += content


    # touch a file for first use ,m
    fname = tempfile.gettempdir() + "/popresource.txt"

    try:
            time.ctime(os.path.getmtime(fname))
            exit(0)
    except OSError as e:
            with file(fname, 'a'):
                    os.utime(fname, None)
                    print "Tempfile stored in %s" % fname

    lasttime = time.ctime(os.path.getmtime(fname))
    print "last modified: %s" % lasttime
    correct = 10

    checklist = []

    for x in range(0,10):
        try:
            rand_num = int(random.uniform(0,len(Questions)))
            
            while rand_num in checklist:
                    rand_num = int(random.uniform(0, len(Questions)))

            checklist.append( rand_num )

            randq = Questions[rand_num]
            print randq[0]
            ans = raw_input("> ")
            if ans != randq[1]:
                    print "The answer is: %s" % randq[1]
                    correct -= 1
        except KeyboardInterrupt:
            os.system("clear")
            exit(1)
        except EOFError:
            os.system("clear")
            exit(1)


    os.system("clear")
    print "Score: %1.2f %d/10" % (correct/10.*100., correct)
