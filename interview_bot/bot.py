#!/usr/bin/env python3
import pyttsx3
import time
import sys
from random import randint
import re

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 165)     # setting up new voice rate

def main():
    with open("questions.txt") as f:
        questions = f.readlines()

    questions = [x.strip() for x in questions]
    questions = [x for x in questions if x != '']
    questions = [re.findall("## .*", x) for x in questions]
    questions = [x[0][3:] for x in questions if x]
    cpt = 0
    while cpt < 3:
        q = questions[randint(0,len(questions))]
        print(q)
        engine.say(q)
        engine.runAndWait()

        for remaining in range(60 * 5, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

        _ = input()


main()
