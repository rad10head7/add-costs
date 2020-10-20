#!/usr/bin/python3

import os

#function to add individual lines in file
def add_costs():

    print("what is the file you would like to add?\nMake sure it is in the current working directory")
    thefile = input("> ")
    directory = os.getcwd()
    myfile = directory+'/'+thefile
    add = 0.0


    with open(myfile) as costs:
        lines = [float(line.strip()) for line in costs]
        for line in lines:
            add += line
        print("The total is:", add)

#function to run as script
def main():
    test = int(input("How many files will you be testing?\n> "))
    while test >= 1:
        add_costs()
        test -= 1

    input("Press enter to exit")

if __name__ == "__main__":
    main()


