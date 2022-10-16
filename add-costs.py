#!/usr/bin/python3

import os

totalFile = 'TOTAL_COSTS.txt'
addedResults = 0.0

# function to find files fo add

def find_files(filename, search_path = '/'):
   result = []

   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

# function to add lines in files
def add_costs(file):
    add = 0.0
    
    myFiles = find_files(file)
    for file in myFiles:
        with open(file, 'r') as costs:
            lines = [float(line.strip()) for line in costs]
            for line in lines:
                add += line
                addedResults += add

#function to run as script
def main():
    test = int(input("How many files will you be testing?\n> "))
    while test >= 1:
        file = input("file name ")
        add_costs(file)
        test -= 1

    f = open(totalFile, 'a')
    f.write(addedResults)
    totalNumber = f.readline()
    print('Here is the sum of all of your files: ' + totalNumber)
    f.close()

    fileDelete = input("Would you like to delete to the file with you total sum of values?
    Y for yes or N for No?")

    fileDelete.upper().strip()

    if fileDelete == 'Y':
        os.remove(totalFile)
        input('File Deleted. Press Enter to exit.')
    else:
        input('Just press enter to exit program. THANKS!')

if __name__ == "__main__":
    main()
