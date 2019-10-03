'''
    Program: Chapter1
    File: Chapter1.py
    Author: Jason J Welch
    Date: Aug 25, 2019
    Purpose:

'''
from ctypes import *
msvcrt = CDLL('msvcrt')
message_string = "Hello world!\n"
msvcrt.printf("Testing: %s", message_string)