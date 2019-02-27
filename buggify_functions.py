import random

def random_line(filelist, opt_arg = 'line_list'):
    '''
    Gets a random line from the file as a string
    (as long as it's not empty or a comment)
    and returns it as a list of characters along with the chosen index.
    '''
    random_line_index = random.randint(0, len(filelist) - 1)

    #To avoid errors, continue to choose a random line until one is retrieved that
    #isn't a comment, isn't empty, isn't full of whitespaces,
    #and isn't the first or last line
    while  (filelist[random_line_index].strip().startswith('#') or
            filelist[random_line_index].strip().startswith("'''") or
            filelist[random_line_index].strip().startswith('"""') or
            len(set(filelist[random_line_index])) <= 1 or
            random_line_index == len(filelist) or
            random_line_index == 0):

            random_line_index = random.randint(0, len(filelist) - 1)
    
    if opt_arg == 'line_list':
        line_list = list(filelist[random_line_index])
        return random_line_index, line_list 
    return random_line_index


def single_char_switch(filelist, num_bugs, char1, char2):
    '''
    Randomly switch two supplied characters for each other once in a line.
    '''
    char_list = [char1, char2]
    line_index, line_char_list = random_line(filelist)
    #line_char_list must contain at least one character from char_list
    while not any(char in char_list for char in line_char_list):
        line_index, line_char_list = random_line(filelist)        
    for char_index, char in enumerate(line_char_list):
        if random.randint(0,2) == 1:     #not too many on same line
            if char == char1:
                line_char_list[char_index] = char2
                num_bugs -=1
            elif char == char2:
                line_char_list[char_index] = char1
                num_bugs -=1   
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


def period_switch(filelist, num_bugs):
    '''
    Randomly switch period to a comma and vice versae.
    '''
    new_filelist, num_bugs_update = single_char_switch(filelist, num_bugs, ',', '.')
    return new_filelist, num_bugs_update
    

def zero_o_switch(filelist, num_bugs):
    '''
    Randomly switch 'o' to a Zero and vice versae.
    '''
    new_filelist, num_bugs_update = single_char_switch(filelist, num_bugs, 'o', '0')
    return new_filelist, num_bugs_update

def elif_else_switch(filelist, num_bugs):
    '''
    Randomly switch 'elif' to 'else' and vice versae.
    '''
    new_filelist, num_bugs_update = single_char_switch(filelist, num_bugs, 'elif', 'else')
    return new_filelist, num_bugs_update

def add_subtract_switch(filelist, num_bugs):
    '''
    Randomly switch '-' to '+' and vice versa.
    '''
    new_filelist, num_bugs_update = single_char_switch(filelist, num_bugs, '+', '-')
    return new_filelist, num_bugs_update

def single_bracket_switch(filelist, num_bugs):
    '''
    Randomly switch one bracket type with another bracket type.
    '''
    bracks_open = ['(','{','[',':',]
    bracks_closed = [')','}',']',';',':']
    if random.randint(0,1) == 0:
        new_filelist, num_bugs_update = single_char_switch(filelist, num_bugs,random.choice(bracks_open), random.choice(bracks_open))
    else:
        new_filelist, num_bugs_update = single_char_switch(filelist, num_bugs,random.choice(bracks_closed), random.choice(bracks_closed))

    return new_filelist, num_bugs_update


def all_char_switch(filelist, char1, char2, char3 = '', char4 = ''):
    '''
    Randomly changes all instances of a character in a line with another one.
    Optional: supply two additional characters for switching in a line.
    '''
    char_list = [char1, char2, char3, char4]
    line_index, line_char_list = random_line(filelist)  

    #line_char_list must contain at least one character from char_list
    while not any(char in char_list for char in line_char_list):
        line_index, line_char_list = random_line(filelist)

    for char_index in range(len(line_char_list)):
        if line_char_list[char_index] == char1:
            line_char_list[char_index] = char2
        elif line_char_list[char_index] == char2:
            line_char_list[char_index] = char1
            
        elif line_char_list[char_index] == char3:
            line_char_list[char_index] = char4
        elif line_char_list[char_index] == char4:
            line_char_list[char_index] = char3
            
    return line_char_list, line_index
    

def all_bracket_switch(filelist, num_bugs):
    '''
    Switches all bracket types in a random line with another bracket type.
    '''
    randomizer = random.randint(0,2)
    if randomizer == 0:
        line_char_list, line_index = all_char_switch(filelist, '(', '[', ')', ']')
    elif randomizer == 1:
        line_char_list, line_index = all_char_switch(filelist, '(', '{', ')', '}')
    elif randomizer == 2:
        line_char_list, line_index = all_char_switch(filelist, '[', '{', ']', '}')
        
    num_bugs -=1
    filelist[line_index] = ''.join(line_char_list)
    return filelist, num_bugs


def bugged_comment(filelist, num_bugs):
    '''
    Replaces comment with a specified comment.
    '''
    bug_comment = '#THIS COMMENT HAS BEEN BUGGIFIED!'
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
    Randomly replaces pre-defined text within triple quotes.
    '''
    doc_list = []
    for line_index in range(len(filelist)):
        if filelist[line_index].strip().startswith("'''") or filelist[line_index].strip().startswith('"""'):
            doc_list.append(line_index)

    if len(doc_list) == 0 or len(doc_list) % 2 != 0:  
        return filelist, num_bugs
    start_quotes = [x for x in doc_list if doc_list.index(x) % 2 == 0]
    end_quotes = [x for x in doc_list if doc_list.index(x) % 2 == 1]
    random_num = (random.randint(0, len(start_quotes))) - 1
    for docstring_line in range(start_quotes[random_num], (end_quotes[random_num]) +1):
        filelist[docstring_line] = '#BUGGIFIED DOCSTRING'.rjust(24)
    num_bugs -= 1
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
    '''
    line_index, line_char_list = random_line(filelist)
    random_index = random.randint(0, len(line_char_list) - 1)

    while (line_char_list[random_index] == ' ' or
           line_char_list[random_index - 1] == ' ' or
           random_index == 0):
        random_index = random.randint(0, len(line_char_list) - 1)
        
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
    for char_index in range(len(line_char_list)):
        if '=' not in line_char_list:
            break
        randomizer = random.randint(0,1)
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
        for char_index in range(len(line_char_list)):
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


#List of all the bugs which buggify randomly chooses from to implement.    
function_list = [
                 bugged_comment,
                 bugged_docstring,
                 tabs_spaces,
                 num_change,
                 zero_o_switch,
                 single_bracket_switch,
                 all_bracket_switch,
                 elif_else_switch,
                 period_switch,
                 add_subtract_switch
                 line_switch,
                 char_switch,
                 case_switch,
                 equal_switch,
                 camel_snake_case,
                 if_switch,
                 ]
