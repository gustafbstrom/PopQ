#!/usr/bin/env python

import sys
import os
import time
import random
import tempfile

class PopQ(object):
    temp_file = "popresource.txt"

    def __init__(self, correct=10):
        self.__correct = correct
        self.correct = correct
        self.questions = list()
        self.checklist = list()
        self.fname = '/'.join([tempfile.gettempdir(), self.temp_file]) # Touch a file for first use
        
        # Import questions and answers
        if len(sys.argv) < 2:
            print "Usage: main.py FILES"
            sys.exit(1)
        for filepath in sys.argv[1:]:
            with open(filepath) as fp:
                print "Opening: ",filepath
                content = eval( fp.read() )
                print "Loaded :",len(content)," questions"
                questions += content

        try:
            time.ctime(os.path.getmtime(self.fname))
            exit(0)
        except OSError as e:
            with file(self.fname, 'a'):
                    os.utime(self.fname, None)
                    print "Tempfile stored in %s" % self.fname

        lasttime = time.ctime(os.path.getmtime(fname))
        print "last modified: %s" % lasttime

    def new_questionarie(self):
        """Start a new questionarie round"""
        self.correct = self.__correct
        for x in range(0, self.__correct):
            try:
                rand_num = int(random.uniform(0, len(questions)))

                while rand_num in checklist:
                    rand_num = int(random.uniform(0, len(questions)))

                checklist.append(rand_num)

                randq = questions[rand_num]
                print randq[0]
                ans = raw_input("> ")
                if ans.lower() != randq[1].lower():
                    print "The answer is: %s" % randq[1]
                    self.correct -= 1
            except KeyboardInterrupt:
                os.system("clear")
                exit(1)
            except EOFError:
                os.system("clear")
                exit(1)
    
    def __str__(self):
        """Presented score string from latest round"""
        return "Score: %1.2f %d/%d" % (self.correct/10.*100., self.correct, self.__correct)

    def print_score(self):
        """Print the core from latest round"""
        os.system("clear")
        print self.score()

if __name__ == "__main__":
    Q = PopQ(10)
    Q.new_questionarie()
    Q.print_score()
