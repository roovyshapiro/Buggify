import shutil, os, difflib, sys, random
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk
import buggify_functions as bf

def copy_file(file):
    '''
    Returns the original file and a copy of the original ('filename.py')
    into the same directory: 'filenameBUGGIFIED.py'
    '''
    buggified_file = alter_file_name(file, 'BUGGIFIED')
    shutil.copy(file, buggified_file)
    return file, buggified_file

def alter_file_name(full_file_path, word_to_insert, opt_arg = 'same_ext'):
    '''
    Returns a filename with a word inserted between a filename and its extension.
    Optional argument of 'text' returns the altered filename as .txt file.
    '''
    path_of_file = os.path.split(full_file_path)
    
    ext_num = len(path_of_file[1]) - path_of_file[1].find('.')
    ext = path_of_file[1][-ext_num:]
    filename = path_of_file[1][:-ext_num]
    if opt_arg == 'same_ext':
        new_filename = filename + word_to_insert + ext
    elif opt_arg == 'text':
        new_filename = filename + word_to_insert + ext + '.txt'
    # Without incrementing new_filename, the file will simply be replaced
    # if buggify() is run multiple times on the same file.
    num_files = 1
    while new_filename in os.listdir():
        new_filename = filename + word_to_insert + "-" + str(num_files) + ext
        num_files += 1
        if opt_arg == 'text':
            new_filename = new_filename + '.txt'
    return new_filename

def convert_to_list(file):
    '''
    Returns the new BUGGIFIED file we created as a list.
    '''
    with open(file) as f:
        filelist = f.read().splitlines()
    return filelist

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

def buggify(num_bugs = 20, full_file_path = ''):
    '''
    Main Buggify function.
    1. Creates copy of file and alters the filename
    2. Runs random bug functions to add errors into the copy of the file
    3. Outputs the answer key diff showing the bugs that were introduced

    Optional Arguments:
    num_bugs: int
        The amount of bugs to introduce.
        Defaults to 20 if left blank.
    full_file_path: string
        The full file path of the file to buggify.
        May leave blank to be prompted to choose file.
    '''
    if full_file_path == '':
        #Removes small Tk window and prompts user to choose file.
        Tk().withdraw()
        full_file_path = askopenfilename()
    original_file, copy_of_file = copy_file(full_file_path)   
    filelist = convert_to_list(copy_of_file)
    #Answer key becomes a .txt file for easier reviewing
    answer_key = alter_file_name(original_file, 'BUG-ANSWERKEY', 'text')
    while num_bugs > 1:
        try:
            random_num = random.randint(0,len(bf.bug_function_list) - 1)
            filelist, num_bugs = bf.bug_function_list[random_num](filelist, num_bugs)
        except ValueError:
            print('buggify() errors!')
            break
    filechanges = '\n'.join(filelist)
    with open(copy_of_file, 'w') as f:
        f.write(filechanges)
    diff_output(original_file, copy_of_file, answer_key)

#call the main function to allow for easy testing
buggify()
