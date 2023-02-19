#--------------------------------------------
#   Name: Jugal Sadhnani 
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 
# You must determine how to structure your solution.
# Create your functions here and call them from under
# if __name__ == "__main__"!

import sys


def demo_command_line():
    """ 
        this function takes a file as input(inputfile), reads the 
        words in the file and then counts each word as they are repeated.
        Then divides each count by the total count to get frequency of each word.
        later writes "word  count  frequency" of each word in a lexicographic order
        onto a file named "inputfile.out".

    """
    # these if statements check if only two arguments are passed, and prints
    # an error message if there are more or less arguments given.
    if len(sys.argv)<2:
        sys.exit("Expected two arguments, got less\n The format is \'python3 freq.py <inputfilename>\'")
    elif len(sys.argv)>2:
        sys.exit("Expected two arguments, got more\n The format is \'python3 freq.py <inputfilename>\'")
    else:
        pass

    file_process()

def file_process():
    """this function takes two arguments, first one being the name of the program
       and the other being the input file name. The function then opens two files,
       the input file and the output file."""

    # the first argument is the program name
    print(sys.argv[0])
    # so the f1 is the second argument
    f1 = open(f"{sys.argv[1]}","r")
    # f2 is the file which we create as we want to write to this file
    f2=open(f"{sys.argv[1]}.out","w")
    # opens the file and does all the process but returns "" if the file is empty or
    # if end of file is reached.
    try:
        line_reader(f1,f2)
    except EOFError:
        return("")

def line_reader(f1,f2):
    """ This function reads the lines from the input file and then adds all the words
       and their count into a dictonary """

    list01=[]
    words={}
    # this assigns the lines in f1 to "line"
    # this is done so we can use it later in our for loops, to iterate over the file
    # list01 stores the words 
    line=f1.readline()
    list01.extend(line.split()) # this only stores the words of the first line

    for lines in f1:
        list01.extend(lines.split())

    # this checks for the different words in list01 and
    # then saves it into a dictonary called words.
    # The dictonary also stores the count of the each word
    # i.e the number of times each word is repeated.
    for i in list01:
        count=0
        for j in list01:
            if i==j:
                count+=1
        words[f"{i}"]=count

    freq_calc(words,f1,f2)

def freq_calc(words,f1,f2):
    """ this function counts the total number of words in the input file and then
       calculates the frequency of each word and then appends it to each word in the
       dictionary """

    total=0
    # total stores the total number of words in the input file
    total=sum(words.values())
    
    # this for loop ensures that each key in the dictonary has two values
    # one being the count of the word and the other being the frequency
    # i.e word=[count,frequency]
    # this stores the frequency in 3decimal place.
    for k in words:
        words[k]=[words[k],round((words[k]/total),3)]

    sort_n_print(words,f1,f2)

def sort_n_print(words,f1,f2):
    """ this function sorts the dictonary in lexicographic order and then writes it
        to the output file as "word-count-frequency" and then closes both the files. """

    # this for loop ensures all the keys in the dictonary "words"
    # is saved in a list called "list03"
    # after all keys have been saved in list03, the sort function has
    # been used to arrange list03 in lexicographic order
    list03=[]
    for key,value in words.items():
        list03.append(key)
        list03.sort()
    
    #this for loop just writes "word count frequency" onto the output file.
    for j in list03:
        f2.write(f"{j} {(words[j])[0]} {(words[j])[1]}\n")

    # both input and output files have been closed.
    f1.close()
    f2.close()


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    demo_command_line()