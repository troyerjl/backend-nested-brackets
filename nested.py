#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "troyerjl and geeks for geeks"

import sys



def main(args):
    with open("input.txt", "r") as f:
        list_of_strings = f.readlines()
    close_brackets = [ ")", "]", "}", ">", "*)" ]
    open_brackets = [ "(", "[", "{", "<", "(*)" ] 
    for string in list_of_strings:
        stack = []
        for i in string:
            if i in open_brackets:
                stack.append(i)
            elif i in close_brackets:
                pos = close_brackets.index(i) 
                if ((len(stack) > 0) and 
                (open_brackets[pos] == stack[len(stack)-1])): 
                    stack.pop()
                else:
                    print("Nos")
        if len(stack) == 0:
            print("Yes")
    

if __name__ == '__main__':
    main(sys.argv)
