## This file can be logically split up into two major sections.
## Section 1 deals with copying the file, changing the file name,
## generating the diff/answer key, and running the actual
## main buggify() function. buggify() chooses from a list of
## "bug functions" to apply to the file at random.
## Section 2 contains these bug functions and is further logically divided
## into three sections: helper functions, main bug functions and
## two global variables.

################################
##### Section 1 - buggify() ####
################################

import shutil, os, difflib, sys, random
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk

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
    with open(file, errors='ignore') as f:
        filelist = f.read().splitlines()
    return filelist

def diff_output(file, bugfile, answers):
    '''
    Returns a diff file between the original file and the buggified file.
    '''

    with open(file, errors='ignore') as f1:
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
    with open(answers,'w', errors='ignore') as f:
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
    #Allow buggify() to take arguments if run from command line.
    #Arguments may be either the filename, the amount of bugs or both.
    #Arguments can be supplied in any order.
    if __name__ == "__main__":
        if len(sys.argv) == 1:
            num_bugs = 20
            full_file_path = ''
        elif len(sys.argv) <= 3:
            for argument in sys.argv[1:]:
                if argument.isnumeric():
                    num_bugs = int(argument)
                elif type(argument) == str:
                    full_file_path = argument
        elif len(sys.argv) < 1 or len(sys.argv) > 3:
            sys.exit("Invalid Arguments!")

    #When this program is imported via the python shell,
    #this is needed to ensure that either single argument may be given.
    if type(num_bugs) == str and type(full_file_path) ==int:
        file = num_bugs
        num = full_file_path
        full_file_path = file
        num_bugs = num
    elif type(num_bugs) == str:
        full_file_path = num_bugs
        num_bugs = 20
        
    #If no file has been specified,
    #Removes small Tk window and prompts user to choose file.
    if full_file_path == '':
        Tk().withdraw()
        full_file_path = askopenfilename()
        
    original_file, copy_of_file = copy_file(full_file_path)   
    filelist = convert_to_list(copy_of_file)
    #Answer key becomes a .txt file for easier reviewing
    answer_key = alter_file_name(original_file, 'BUG-ANSWERKEY', 'text')
    while num_bugs > 1:
        try:
            random_num = random.randint(0,len(bug_function_list) - 1)
            filelist, num_bugs = bug_function_list[random_num](filelist, num_bugs)
        except ValueError:
            print('WARNING! ValueError: buggify() may not have run successfully on ' + original_file)
            break
    filechanges = '\n'.join(filelist)
    with open(copy_of_file, 'w', errors='ignore') as f:
        f.write(filechanges)
    diff_output(original_file, copy_of_file, answer_key)


#########################################
#### Section 2 - bug_function_list[] ####
#########################################


####  The primary purpose of this section is
####  the global list variable, bug_function_list.
####  buggify() in Section 1 chooses functions at random 
####  from this list to affect the buggified file.
####
####  This file can be logically divided into three sub-sections.
####     2-1. Helper Functions - Functions that are used by other functions
####        in Section 2-2
####     2-2. Bug Functions - The functions that are present in  
####          bug_function_list which actually apply the bugs
####     2-3. Global Variables


##
## Section 2-1. Helper Functions 
##
## These functions are used by the other functions in global bug_function_list
##

def random_line(filelist, opt_arg = 'line_list'):
    '''
    Gets a random line from the file as a string
    (as long as it's not a comment, part of a docstring,
    empty, the first line or the last line, or the second to last line)
    and returns it as a list of characters along with the chosen index.
    '''
    random_line_index = random.randint(0, len(filelist) - 1)
    global docstring_line_indexes
    if docstring_line_indexes == []:
        docstring_line_indexes = docstring_detect(filelist)

    while (filelist[random_line_index].strip().startswith('#') or
        random_line_index in docstring_line_indexes or
        len(set(filelist[random_line_index])) <= 2 or
        random_line_index >= (len(filelist) - 1) or
        random_line_index == 0):

            random_line_index = random.randint(0, len(filelist) - 1)
    
    if opt_arg == 'line_list':
        line_list = list(filelist[random_line_index])
        return random_line_index, line_list 
    return random_line_index

def multi_char_switch(filelist, num_bugs, chars1, chars2, func_name = ''):
    '''
    Switches two supplied characters or words for each other once in a line.
    They do not have to be the same length.
    '''
    line_index, line_char_list = random_line(filelist)
    
    #line_char_list must contain at least either chars1 or char2
    #Break the loop if it tries more than 100 times to prevent
    #a situation where the word or character isn't present in the file.
    #If a line can't be found, then that function is removed from the main
    #bug_function_list to ensure it isn't run again.
    line_search_tries = 100
    while chars1 not in filelist[line_index] or chars2 not in filelist[line_index]:
        line_index, line_char_list = random_line(filelist)
        line_search_tries -= 1
        if line_search_tries == 0:
            if func_name != '':
                global bug_function_list
                bug_function_list.remove(func_name)
            return filelist, num_bugs
        
    for char_index in range(len(line_char_list)):
        if random.randint(0,2) == 1:     #not too many on same line
            if line_char_list[char_index : char_index + len(chars1)] == list(chars1):
                line_char_list[char_index : char_index + len(chars1)] = chars2
                num_bugs -=1
            elif line_char_list[char_index : char_index + len(chars2)] == list(chars2):
                line_char_list[char_index : char_index + len(chars2)] = chars1
                num_bugs -=1   
    filelist[line_index] = ''.join(line_char_list)
    return filelist, num_bugs

def all_char_switch(filelist, num_bugs, char1, char2, char3 = '', char4 = '', func_name = ''):
    '''
    Randomly changes all instances of a character in a line with another one.
    Optional: supply two additional characters for switching in a line.
    '''
    char_list = [char1, char2, char3, char4]
    line_index, line_char_list = random_line(filelist)  
    #line_char_list must contain at least one character from char_list
    #Break the loop if it tries more than 50 times to prevent
    #a situation where the characters aren't present in the file.
    #If a line can't be found, then the function is removed from the main
    #bug_function_list to ensure it isn't run again.
    line_search_tries = 100
    while not any(char in char_list for char in line_char_list):
        line_index, line_char_list = random_line(filelist)
        line_search_tries -= 1
        if line_search_tries == 0:
            if func_name != '':
                global bug_function_list
                bug_function_list.remove(func_name)
            return filelist, num_bugs

    for char_index in range(len(line_char_list)):
        if line_char_list[char_index] == char1:
            line_char_list[char_index] = char2
        elif line_char_list[char_index] == char2:
            line_char_list[char_index] = char1
            
        elif line_char_list[char_index] == char3:
            line_char_list[char_index] = char4
        elif line_char_list[char_index] == char4:
            line_char_list[char_index] = char3
    num_bugs -= 1
    filelist[line_index] = ''.join(line_char_list)
            
    return filelist, num_bugs

def docstring_detect(filelist, return_start_end = 'no'):
    '''
    This function detects all the lines of a docstring.
    This is useful because we don't want most of the bugs to apply to docstrings.
    To detect a full docstring:
    1. Append all line indexes which start with triple quotes to a list.
    2. If the len(list) is even, we know that we have the beginnings and endings of the docstrings.
       If it's not even, the docstrings are either formatted incorrectly, or this function won't work.
    3. Append the 0, 2, 4 etc. list indexes to [start_quotes], which will be our docstring starts.
    4. Append the 1, 3, 5 etc. list indexes to [end_quotes], which will be our docstring ends.
    5. A range is then calculated from the 0 index of start_quotes to the 0 index of [end_quotes].
    Example:
    doc_list = [1, 3, 8, 10] #These lines begin with triple quotes.
    start_quotes = [1,8]
    end_quotes = [3,10]
    Lines 1, 2, 3 are a docstring. Lines 8, 9, 10 are another docstring.
    full_doc_list of [1,2,3,8,9,10] is returned.

    return_start_end == 'no'
    This is for the bugged_docstring() function which should only apply to a single docstring.
    Either lines 1 through 3, or lines 8 through 10.
    '''
    doc_list = []
    start_quotes = []
    end_quotes = []
    full_doc_list = []
    
    for line_index in range(len(filelist)):
        if filelist[line_index].strip().startswith("'''") or filelist[line_index].strip().startswith('"""'):
            doc_list.append(line_index)
        else:
            continue
    if len(doc_list) == 0 or len(doc_list) % 2 != 0:
        if return_start_end == 'yes':
            return start_quotes, end_quotes
        full_doc_list.append(0)
        return full_doc_list
    start_quotes = [num for num in doc_list if doc_list.index(num) % 2 == 0]
    end_quotes = [num for num in doc_list if doc_list.index(num) % 2 == 1]    
    for x in range(len(start_quotes)):
        for y in range(start_quotes[x], end_quotes[x] + 1):
            full_doc_list.append(y)
    global docstring_line_indexes
    if docstring_line_indexes == []:
        docstring_line_indexes = full_doc_list
    if return_start_end == 'yes':
        return start_quotes, end_quotes
    return full_doc_list   


##
##  Section 2-2. Bug Functions
##
##  The functions that are present in global bug_function_list 
##  which actually apply the bugs
##


def period_switch(filelist, num_bugs):
    '''
    Randomly switch period to a comma and vice versae.
    '''
    new_filelist, num_bugs_update = multi_char_switch(filelist, num_bugs, ',', '.', period_switch)
    return new_filelist, num_bugs_update
    
def zero_o_switch(filelist, num_bugs):
    '''
    Randomly switch 'o' to a Zero and vice versae.
    '''
    new_filelist, num_bugs_update = multi_char_switch(filelist, num_bugs, 'o', '0', zero_o_switch)
    return new_filelist, num_bugs_update

def elif_else_switch(filelist, num_bugs):
    '''
    Randomly switch 'elif' to 'else' and vice versae.
    '''
    new_filelist, num_bugs_update = multi_char_switch(filelist, num_bugs, 'elif', 'else', elif_else_switch)
    return new_filelist, num_bugs_update

def add_subtract_switch(filelist, num_bugs):
    '''
    Randomly switch '-' to '+' and vice versa.
    '''
    new_filelist, num_bugs_update = multi_char_switch(filelist, num_bugs, '+', '-', add_subtract_switch)
    return new_filelist, num_bugs_update

def single_bracket_switch(filelist, num_bugs):
    '''
    Randomly switch one bracket type with another bracket type.
    '''
    bracks_open = ['(','{','[',':',]
    bracks_closed = [')','}',']',';',':']
    if random.randint(0,1) == 0:
        new_filelist, num_bugs_update = multi_char_switch(filelist, num_bugs,random.choice(bracks_open), random.choice(bracks_open), single_bracket_switch)
    else:
        new_filelist, num_bugs_update = multi_char_switch(filelist, num_bugs,random.choice(bracks_closed), random.choice(bracks_closed), single_bracket_switch)
    return new_filelist, num_bugs_update

def all_bracket_switch1(filelist, num_bugs):
    '''
    Switches all bracket types in a random line with another bracket type.
    '''
    filelist, num_bugs = all_char_switch(filelist, num_bugs, '(', '[', ')', ']', func_name = all_bracket_switch1)
    return filelist, num_bugs

def all_bracket_switch2(filelist, num_bugs):
    '''
    Switches all bracket types in a random line with another bracket type.
    '''
    filelist, num_bugs = all_char_switch(filelist, num_bugs, '(', '{', ')', '}', func_name = all_bracket_switch2)
    return filelist, num_bugs

def all_bracket_switch3(filelist, num_bugs):
    '''
    Switches all bracket types in a random line with another bracket type.
    '''
    filelist, num_bugs = all_char_switch(filelist, num_bugs, '[', '{', ']', '}', func_name = all_bracket_switch3)
    return filelist, num_bugs

def line_switch(filelist, num_bugs):
    '''
    Randomly switch a line with the one before it.
    '''   
    random_line_index = random_line(filelist, 'no_line_list')

    first_line = filelist[random_line_index]
    second_line = filelist[random_line_index - 1]
    
    filelist[random_line_index] = second_line
    filelist[random_line_index - 1] = first_line
    
    num_bugs -= 1
    return filelist, num_bugs

def char_switch(filelist, num_bugs):
    '''
    Switch a randomly chosen character with the one before it,
    provided the character chosen isn't the first index
    and its previous character is not a white space.
    If a line is found with no consecutive characters,
    the while loop will be stuck trying to find a character
    whose previous character isn't a whitespace. After trying 50 times,
    it will simply switch the character with a white space and move on.
    '''
    line_index, line_char_list = random_line(filelist)
    random_index = random.randint(0, len(line_char_list) - 1)
    tries = 0
    while (line_char_list[random_index] == ' ' or
           line_char_list[random_index - 1] == ' ' or
           random_index == 0):
        random_index = random.randint(0, len(line_char_list) - 1)
        tries += 1
        if tries == 50:
            break        
    char = line_char_list[random_index] 
    prev_char = line_char_list[random_index - 1]
    
    line_char_list[random_index - 1] = char
    line_char_list[random_index] = prev_char
    
    num_bugs -= 1

    filelist[line_index] = ''.join(line_char_list)
    return filelist, num_bugs
    
def case_switch(filelist, num_bugs):
    '''
    Randomly switch the first character in a word from lower to upper and vice versae.
    '''
    num_times = num_bugs
    while num_times == num_bugs:
        line_index, line_char_list = random_line(filelist)
        for char_index in range(len(line_char_list)):
            randomizer = random.randint(0, 3)
            if ' ' not in line_char_list:
                if line_char_list[0].isupper():
                    line_char_list[0] = line_char_list[0].lower()
                elif line_char_list[0].islower():
                    line_char_list[0] = line_char_list[0].upper()
                num_bugs -= 1
                break
            if line_char_list[char_index].isalpha() and line_char_list[char_index - 1] == ' ' and randomizer == 1:
                if line_char_list[char_index].isupper():
                    line_char_list[char_index] = line_char_list[char_index].lower()
                elif line_char_list[char_index].islower():
                    line_char_list[char_index] = line_char_list[char_index].upper()
                num_bugs -= 1
                break
    filelist[line_index] = ''.join(line_char_list)
    return filelist, num_bugs

def equal_switch(filelist, num_bugs):
    '''
    Switch '=' to '==' and vice versae
    '''
    line_index, line_char_list = random_line(filelist)
    line_search_tries = 100
    #If a line containing an '=' can't be found after 100 tries,
    #remove this function from the list so it can't be run again.
    while '=' not in line_char_list:
        line_index, line_char_list = random_line(filelist)
        line_search_tries -= 1
        if line_search_tries == 0:
            global bug_function_list
            bug_function_list.remove(equal_switch)
            return filelist, num_bugs
        
    randomizer = random.randint(0,1)
    for char_index in range(len(line_char_list) - 1):
        if (line_char_list[char_index] == '=' and
            line_char_list[char_index + 1] == '=' and
            randomizer == 0):           
            line_char_list[char_index + 1] = ''
            num_bugs -= 1
            break
        elif (line_char_list[char_index] == '=' and
              #prevent '==' -> '===', '!=' -> '!==', '+=' -> '+==' , '-=' -> '-=='
              line_char_list[char_index + 1] != '=' and
              line_char_list[char_index - 1] not in ['=','!','+','-'] and 
              randomizer == 1):            
            line_char_list.insert(char_index + 1, '=')
            num_bugs -= 1
            break
    filelist[line_index] = ''.join(line_char_list)
    return filelist, num_bugs

def if_switch(filelist, num_bugs):
    '''
    This function either:
    Removes an 'if' from the beginning of a line
    and the ':' from the end of a line,
    OR adds an 'if' to the beginning and ':' to the end of the line,
    and indents the following line with four additional spaces
    '''
    #Get random line index from the line
    #and doesn't return the line as a list of characters
    random_line_index = random_line(filelist, 'no_line_list')

    #Remove whitespaces from end of line to ensure that the ':' is the [-1] index.       
    filelist[random_line_index] = filelist[random_line_index].rstrip()

    #If 'if' is in the line and the last character is ':'
    #delete if, ':' and a whitespace character if that line is indented
    if filelist[random_line_index][-1] == ':':
        if 'if' in filelist[random_line_index] and 'elif' not in filelist[random_line_index]:
            if_index = filelist[random_line_index].index('if')
            line_list = list(filelist[random_line_index])
            del line_list[if_index + 1]
            del line_list[if_index]
            del line_list[-1]
            if line_list[0] == ' ':
                del line_list[0]
            filelist[random_line_index] = ''.join(line_list)

    #If the last character is not a ':',
    #Add an 'if' after the initial whitespaces with a colon at the end.
    #Additionally, add four white spaces to the beginning of the next line
    elif filelist[random_line_index][-1] != ':' and filelist[random_line_index + 1] != '':
        line_list = list(filelist[random_line_index]) 
        for char_index in range(len(line_list)):
            if line_list[char_index] == ' ':
                continue
            else:
                line_list.insert(char_index, 'i')
                line_list.insert(char_index + 1, 'f')
                line_list.insert(char_index + 2, ' ')
                line_list.append(':')
                filelist[random_line_index] = ''.join(line_list)
                break
        next_line_list = list(filelist[random_line_index + 1])
        for x in range(4):
            next_line_list.insert(0, ' ')
        filelist[random_line_index + 1] = ''.join(next_line_list)
        
    num_bugs -= 1
    return filelist, num_bugs

def camel_snake_case(filelist, num_bugs):
    '''
    Converts snake_case to camelCase and vice versae.
    '''
    line_index, line_char_list = random_line(filelist)

    #If the line contains at least one underscore,
    #For every underscore in the line,
    #the letter before the underscore is capitalized
    #and the underscore is removed.
    #All the changes made in this line are counted as one num_bug.
    if '_' in line_char_list:
        for char_index in range(len(line_char_list) - 1):
            if line_char_list[char_index] == '_':
                line_char_list[char_index + 1] = line_char_list[char_index + 1].upper()
                line_char_list[char_index] = ''
        num_bugs -= 1
    #Else if the line contains no underscores,
    #For every uppercase letter in the line which has an alphanumeric character before it,
    #each uppercase letter is made lower case with an underscore inserted before it.
    #All the changes made in this line are counted as one num_bug.
    elif '_' not in line_char_list:
        for char_index in range(len(line_char_list)):
            if line_char_list[char_index].isupper() and line_char_list[char_index - 1].isalnum():
                line_char_list.insert(char_index, '_')
                line_char_list[char_index + 1] = line_char_list[char_index + 1].lower()
        num_bugs -= 1

    filelist[line_index] = ''.join(line_char_list)
    return filelist, num_bugs

def tabs_spaces(filelist, num_bugs):
    '''
    Randomly adds or subtracts a space in a tabbed line,
    or adds a tab or double tab where it doesn't belong.
    '''
    line_index, line_char_list = random_line(filelist)
    randomizer = random.randint(0,2)
    if line_char_list[:4] == [' ', ' ', ' ', ' ']:
        if randomizer == 0:
            line_char_list.insert(0, ' ')
        elif randomizer == 1:
            del line_char_list[0]
        elif randomizer == 2:
            for x in range(4):
                line_char_list.insert(0, ' ')
    else:
        for x in range(4):
            line_char_list.insert(0, ' ')

    num_bugs -=1
    filelist[line_index] = ''.join(line_char_list)
    return filelist, num_bugs

def num_change(filelist, num_bugs):
    '''
    Randomly adds or subtracts an int by 1.
    '''
    line_index, line_char_list = random_line(filelist) 
    for char_index in range(len(line_char_list)):
        randomizer = random.randint(0,2)
        if line_char_list[char_index].isdigit() and randomizer != 2:
            line_char_list[char_index] = int(line_char_list[char_index])
            if line_char_list[char_index] == 0:
                line_char_list[char_index] += 1
            elif randomizer == 0:
                line_char_list[char_index] += 1
            elif randomizer == 1:
                line_char_list[char_index] -= 1
            num_bugs -= 1
            line_char_list[char_index] = str(line_char_list[char_index])
            break
        else:
            continue
    filelist[line_index] = ''.join(line_char_list)
    return filelist, num_bugs

def missing_blanks(filelist, num_bugs):
    '''
    Replaces 1/3 of the non-whitespace characters in a line with underscores.
    
    Attempts to find a line with less than 5 underscores.
    If no such line is found after 20 tries, this function is removed from the list.
    Otherwise, the whole file becomes full of underscores
    when running this a large amount of times.
    '''
    line_index, line_char_list = random_line(filelist)
    line_search_tries = 20
    while line_char_list.count('_') > 5:
        line_index, line_char_list = random_line(filelist)
        line_search_tries -= 1
        if line_search_tries == 0:
            global bug_function_list
            bug_function_list.remove(missing_blanks)
            return filelist, num_bugs

    spaceless_char_list = [index for index, value in enumerate(line_char_list) if value != ' ']
    for char in range(len(line_char_list) // 3):
        line_char_list[random.choice(spaceless_char_list)] = '_'
    filelist[line_index] = ''.join(line_char_list) + " #Fill in the missing blanks!"
    num_bugs -=1
    return filelist, num_bugs
    
def scrambled_line(filelist, num_bugs):
    '''
    Rearranges all the words in a random line.
    
    Words are defined as being separated by whitespaces.
    random_line() is called here with the 'no_line_list' argument
    so that a full line is returned instead of a list of characters.
    
    Attempt to find a line with at least 4 words.
    If no such line is found after 50 tries, then this function is removed.
    
    Unfortunately, .split() removes the whitespaces from
    the beginning of the line.
    Therefore, beginning whitespaces are counted up and added
    to the beginning of the line.
    '''
    random_line_index = random_line(filelist, 'no_line_list')
    line_list = filelist[random_line_index].split()

    line_search_tries = 50
    while len(line_list) < 4:
        random_line_index = random_line(filelist, 'no_line_list')
        line_list = filelist[random_line_index].split()
        line_search_tries -= 1
        if line_search_tries == 0:
            global bug_function_list
            bug_function_list.remove(scrambled_line)
            return filelist, num_bugs
        
    num_spaces = 0
    for char in filelist[random_line_index]:
        if char == ' ':
            num_spaces += 1
        else:
            break
    random.shuffle(line_list)
    filelist[random_line_index] = (num_spaces * ' ') + ' '.join(line_list) + " #Scrambled line!"
    num_bugs -=1
    return filelist, num_bugs
	
def bugged_comment(filelist, num_bugs):
    '''
    Replaces comment with a specified comment.
    '''
    bug_comment = '#BUGGIFIED COMMENT'
    for line_index in range(len(filelist)):
        #Prevents conflict with bugged_docstring()
        if 'DOCSTRING' in filelist[line_index] or '#' not in filelist[line_index]:
            continue
        hash_index = filelist[line_index].index('#')
        #A '#" without a white space prior to it is not considered a comment
        #Take ".index('#')" in the previous line as an example
        if filelist[line_index][hash_index - 1].isspace() and random.randint(1, 3) == 1:
            line_list = list(filelist[line_index])
            filelist[line_index] = ''.join(line_list[:hash_index]) + bug_comment
            num_bugs -= 1
            break
    return filelist, num_bugs

def bugged_docstring(filelist, num_bugs):
    '''
    Replaces the lines of a random docstring with #BUGGIFIED DOCSTRING
    '''
    start_quotes, end_quotes = docstring_detect(filelist, return_start_end = 'yes')
    if start_quotes != [] or end_quotes != []:
        random_index = (random.randint(0, len(start_quotes))) - 1
        for docstring_line in range(start_quotes[random_index], (end_quotes[random_index]) + 1):
            filelist[docstring_line] = '#BUGGIFIED DOCSTRING'.rjust(24)
        num_bugs -= 1
    return filelist, num_bugs


##
##  Section 2-3. Global Variables
##
##  These variables are refernced globally by other functions.
##


#This list gets populated with the lines of all the file's docstrings
#by the docstring_detect() function. It is populated once when the program is run
#and then should be unchanged.
#random_line() uses this list to ensure that the bugs its introducing doesn't apply to docstrings.
#bugged_docstring() doesn't reference this list directly, but does use docstring_detect()
#to determine which lines are docstrings.
docstring_line_indexes = []

#This list contains all the bugs which buggify() chooses from to implement.
#The following functions reference this list in order to remove themselves from it if they can't be applied:
#equal_switch(), missing_blanks(), scrambled_line() and any function which uses
#multi_char_switch() and all_char_switch().
bug_function_list = [
                    period_switch,
                    zero_o_switch,
                    elif_else_switch,
                    add_subtract_switch,
                    single_bracket_switch,
                    all_bracket_switch1,
                    all_bracket_switch2,
                    all_bracket_switch3,
                    line_switch,
                    char_switch,
                    case_switch,
                    equal_switch,
                    if_switch,
                    camel_snake_case,
                    tabs_spaces,
                    num_change,
                    missing_blanks,
                    scrambled_line,
                    bugged_comment,
                    bugged_docstring,
                    ]


#Run the program
if __name__ == "__main__":
    buggify()
    
