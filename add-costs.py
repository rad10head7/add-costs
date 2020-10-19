#!/usr/bin/python3

import os


def add_costs():

    print("what is the file you would like to add?\nMake sure it is in the home directory")
    thefile = input("> ")
    directory = os.getcwd()
    myfile = directory+'/'+thefile
    add = 0.0


    with open(myfile) as costs:
        lines = [float(line.strip()) for line in costs]
        for line in lines:
            add += line
        print("The total is:", add)

    return add


def write_to_file(answer):
    

def main():
    cost = []
    test = int(input("How many files will you be testing?\n> "))
    while test >= 1:
        new_cost = add_costs()
        cost.append(new_cost)
        test -= 1

    do_file = input("Would you like to add the total(s) to a file? (y/n)\n>")

if __name__ == "__main__":
    main()
