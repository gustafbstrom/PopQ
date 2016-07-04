#!/usr/bin/env python

import sys
import os
import time
import random
import tempfile
import argparse

import Menu

class PopQ(object):
    resource_prefix = '/tmp/'
    temp_file = "popresource.txt"

    def _create_nonexisting_resourcefile(self, resource_file_path):
        if not os.path.isfile(resource_file_path):
           open(resource_file_path).close() 

    def _configure_popq(self, args):
        self.question_files = args.question_files
        if args.resource_file:
            self.resource_file_path = args.resource_file
        else:
            self.resource_file_path = self.resource_prefix + self.temp_file

    def __init__(self, correct=10):

        self.__correct = correct
        self.correct = correct
        self.questions = list()
        self.checklist = list()
        self.fname = '/'.join([tempfile.gettempdir(), self.temp_file]) # Touch a file for first use
        self.n_questions = 0
        self.total = 1

        parser = argparse.ArgumentParser(description = 'PopQ - TUI pop quiz application')
        parser.add_argument('-q', '--question_files', nargs='+', required = True, type = str)
        parser.add_argument('-r', '--resource_file', type = str)
        self._configure_popq(parser.parse_args())

        self._create_nonexisting_resourcefile(self.resource_file_path)

        print("Resource file: " + self.resource_file_path)

        for filepath in self.question_files:
            with open(filepath) as fp:
                print "Opening: ",filepath
                fp_code = fp.read()
                if fp_code:
                    content = eval(fp_code)
                    print "Loaded :",len(content)," questions"
                    self.questions += content
                    self.n_questions += len(content)
                else:
                    print "Error while importing %s" % filepath
        try:
            time.ctime(os.path.getmtime(self.fname))
            #exit(0) # Why?
        except OSError as e:
            with file(self.fname, 'a'):
                os.utime(self.fname, None)
                print "Tempfile stored in %s" % self.fname

        lasttime = time.ctime(os.path.getmtime(self.fname))
        print "last modified: %s" % lasttime

    def new_questionnaire(self):
        """Start a new questionnaire round"""
        self.correct = min(self.__correct, self.n_questions)
        self.total = self.correct
        for x in range(0, min(self.__correct, self.n_questions)):
            try:
                rand_num = int(random.uniform(0, len(self.questions)))

                while rand_num in self.checklist:
                    rand_num = int(random.uniform(0, len(self.questions)))

                self.checklist.append(rand_num)

                randq = self.questions[rand_num]
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
        return "Score: %1.2f%s [%d/%d]" % (float(self.correct)/self.total*100.,\
            '%', self.correct, self.total)

    def print_score(self):
        """Print the core from latest round"""
        os.system("clear")
        print self.__str__()

if __name__ == "__main__":
    Q = PopQ(10)
    Q.new_questionnaire()
    Q.print_score()
