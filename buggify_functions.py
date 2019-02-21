import random

def random_line(filelist):
    '''
    Gets a random line from the file as a string
    (as long as it's not empty or a comment)
    and returns it as a list of characters along with the chosen index.
    '''
    line_list = []
    while not line_list:
        #An index of Zero will result in ValueError so it's set to zero to avoid the error.
        try: 
            random_line_index = random.randint(0, len(filelist) - 1)
        except ValueError:
            random_line_index = 0
        if (filelist[random_line_index].strip().startswith('#') and
            filelist[random_line_index].strip().startswith("'''") and
            filelist[random_line_index].strip().startswith('"""')):
            continue
        else:
            line_list = list(filelist[random_line_index])
    return random_line_index, line_list


def single_char_switch(filelist, num_bugs, char1, char2):
    '''
    Randomly switch two supplied characters for each other.
    '''
    line_index, line_char_list = random_line(filelist) 
    line_char_list = filelist[line_index].split(' ')
    for x in range(len(line_char_list)):
        randomizer = random.randint(0,1)   #not too many on same line
        if randomizer == 1:
            if char1 in line_char_list[x]:
                line_char_list[x] = line_char_list[x].replace(char1, char2)
                num_bugs -=1
                break
            elif char2 in line_char_list[x]:
                line_char_list[x] = line_char_list[x].replace(char2, char1)
                num_bugs -=1
                break
        elif randomizer == 0:
            continue        
    filelist[line_index] = ' '.join(line_char_list)
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

def parentheses_switch(filelist, num_bugs):
    '''
    Randomly switch brackets, parentheses_switch and curly braces with each other.
    '''
    bracks_open = ['(','{','[',':',]
    bracks_closed = [')','}',']',';',':']
    randomizer = random.randint(0,1)
    if randomizer:
        new_filelist, num_bugs_update = single_char_switch(filelist, num_bugs,random.choice(bracks_open), random.choice(bracks_open))
    else:
        new_filelist, num_bugs_update = single_char_switch(filelist, num_bugs,random.choice(bracks_closed), random.choice(bracks_closed))

    return new_filelist, num_bugs_update

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
    for line in range(len(filelist)):
        if filelist[line].strip().startswith("'''") or filelist[line].strip().startswith('"""'):
            doc_list.append(line)

    if len(doc_list) == 0 or len(doc_list) % 2 != 0:  
        return filelist, num_bugs
    start_quotes = [x for x in doc_list if doc_list.index(x) % 2 == 0]
    end_quotes = [x for x in doc_list if doc_list.index(x) % 2 == 1]
    random_num = (random.randint(0, len(start_quotes))) - 1
    for y in range(start_quotes[random_num], (end_quotes[random_num]) +1):
        filelist[y] = '#BUGGIFIED DOCSTRING'.rjust(24)
    num_bugs -= 1
    return filelist, num_bugs

def line_switch(filelist, num_bugs):
    '''
    Randomly switch a line with the one before it.
    '''
    randomizer = random.randint(0, len(filelist) - 1)
    first_line = filelist[randomizer]
    #restart the function if one the lines is empty
    if filelist[randomizer] == '' or filelist[randomizer - 1] == '':
        line_switch(filelist, num_bugs)
    #we can't pick the previous line if the first line is chosen
    if randomizer == 0:
        second_line = filelist[randomizer + 1]
        filelist[randomizer] = second_line
        filelist[randomizer + 1] = first_line
    else:
        second_line = filelist[randomizer - 1]
        filelist[randomizer] = second_line
        filelist[randomizer - 1] = first_line
    num_bugs -= 1
    return filelist, num_bugs

def char_switch(filelist, num_bugs):
    '''
    Randomly switch a character with the one before it.
    '''
    line_index, line_char_list = random_line(filelist)
    random_num = random.randint(0, len(line_char_list) - 1)

    #don't switch with whitespace
    if line_char_list[random_num] == ' ' or line_char_list[random_num - 1] == ' ':
        char_switch(filelist, num_bugs)
    char = line_char_list[random_num]
    #we can't use the previous char, if the first char is chosen
    if random_num != 0: 
        prev_char = line_char_list[random_num - 1]
        line_char_list[random_num - 1] = char
    else:
        prev_char = line_char_list[random_num + 1]
        line_char_list[random_num + 1] = char
    line_char_list[random_num] = prev_char
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
 

    

#List of all the bugs which buggify randomly chooses from to implement.    
function_list = [
                 bugged_comment,
                 bugged_docstring,
                 tabs_spaces,
                 num_change,
                 zero_o_switch,
                 parentheses_switch,
                 elif_else_switch,
                 period_switch,
                 line_switch,
                 char_switch,
                 case_switch,
                 equal_switch,
                 ]
