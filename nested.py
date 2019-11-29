#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "troyerjl and geeks for geeks"

import sys

def helper_funct_read_file():
    with open("input.txt", "r") as f:
        list_of_strings = f.readlines()
    list_of_strings = [s.strip("\n") for s in list_of_strings]
    return list_of_strings

def helper_funct_logic(string):
    close_brackets = [ ")", "]", "}", ">", "*)" ]
    open_brackets = [ "(", "[", "{", "<", "(*" ] 
    stack = []
    count_token = 0
    while string:
        i = string[0]
        if string.startswith("(*"):
            i = "(*"
        elif string.startswith("*)"):
            i = "*)"
        string = string[len(i):]
        count_token += 1
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i) 
            if stack and (open_brackets[pos] == stack[-1]): 
                stack.pop()
            else:
                return "No " + str(count_token)            
    if len(stack) == 0:
        return "Yes"
    else: 
        return "No " + str(count_token + 1)       

def main(args):
    lines = helper_funct_read_file()
    for line in lines:
        result = helper_funct_logic(line)
        print(result)

if __name__ == '__main__':
    main(sys.argv)
