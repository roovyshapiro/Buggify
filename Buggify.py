##  Buggify is a Python Bugger which automatically inserts random syntax bugs into a program.
##
##  Authored by Roovy Shapiro
##
##  Here's a basic overview of how the program works:
##
##  1. Choose a file and the number of bugs you'd like to introduce.
##  2. The file is copied to a new file with "BUGGIFIED" appended to the file name before the extension.
##  3. The number of bugs chosen acts as the range in a for loop
##      which randomly calls on a list of bug functions to insert into the new copied file.
##  4. Once completed, a diff is stored showing the differences between the original file and Buggified file.
##  5. The diff is stored as a new file and renamed with "BUG-ANSWERKEY" appended to the file name before the extension.


import shutil, os, difflib, sys, random
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk
import buggify_functions as bf

def buggify():
    '''
    Prompts user to choose a file.
    Add 'BUGGIFIED' to a copy of the file before it's extension.
    Returns the original file and the copy for us to work with.
    '''
    #Removes small tk window
    Tk().withdraw()

    #Prompts User to Choose File.
    file = askopenfilename()

    #Makes a copy of the original ('filename.py') into the same directory 'filenameBUGGIFIED.py'
    buggified_file = alter_file_name(file, 'BUGGIFIED')
    shutil.copy(file, buggified_file)

    return file, buggified_file

def alter_file_name(full_file_path, word_to_insert):
    '''
    Returns a filename with a word inserted between a filename and its extension.
    '''
    path_of_file = os.path.split(full_file_path)
    
    ext_num = len(path_of_file[1]) - path_of_file[1].find('.')
    ext = path_of_file[1][-ext_num:]
    filename = path_of_file[1][:-ext_num]
    
    new_filename = filename + word_to_insert + ext
    return new_filename


def convert_to_list(file):
    '''
    Returns the new BUGGIFIED file we created as a list.
    '''
    with open(file) as f:
        filelist = f.read().splitlines()
    return filelist


def write_changes(file, filechanges):
    '''
    Writes the changes we made to our file.
    '''
    with open(file, 'w') as f:
        f.write(filechanges)
    return file

def diff_output(file, bugfile, answers):
    '''
    Returns a diff file between the original file and the buggified file.
    '''
    with open(file) as f1:
        f1_txt = f1.read().splitlines()
        with open(bugfile) as f2:
            f2_txt = f2.read().splitlines()
            diff = difflib.unified_diff(
                f1_txt,
                f2_txt,
                fromfile='f1.txt',
                tofile='f2.txt',
                n = 0,
                )
    with open(answers,'w') as f:
        for line in diff:
            f.write(line)
            f.write('\n')
    return answers



original_file, copy_of_file = buggify()
filelist = convert_to_list(copy_of_file)
answer_key = alter_file_name(original_file, 'BUG-ANSWERKEY')

num_bugs = 20
while num_bugs > 1:
    random_num = random.randint(0,len(bf.function_list) - 1)
    filelist, num_bugs = bf.function_list[random_num](filelist, num_bugs)
    
filechanges = '\n'.join(filelist)

finalbugs = write_changes(copy_of_file, filechanges)
diff_output(original_file, copy_of_file, answer_key)



