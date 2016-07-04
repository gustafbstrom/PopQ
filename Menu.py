#!/usr/bin/env python

import sys
import os

class Menu(object):
    '''Create and maintain a simple menu for PopQ'''
    program_name = 'PopQ'

    def __init__(self):
        self.choices = {'1': self.add_questions, '2': self.start_questionnaire, 'x': self.exit_program}

    def add_choices(self):
        '''Add more question files to PopQ'''
        pass

    def start_questionnaire(self):
        '''Start a questionnaire session'''
        pass

    def exit_program(self):
        '''Terminate PopQ'''
        pass

    def get_choice(self):
        '''Get and validate some menu input'''
        self.print_menu()
        ans = ''
        while ans.lower() not in self.choices:
            ans = input('> ')
        return ans

    def print_menu(self):
        '''Print PopQ menu'''
        os.system("clear")
        print('\n'.join([self.program_name,'-'*len(self.program_name)]) + \
'''
    1) Choose categories
    2) Start questionnaire
    X) Quit
''')
    def start_menu_loop(self):
        '''Create and maintain the menu input/output'''
        pass
