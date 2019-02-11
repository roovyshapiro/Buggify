import random

def random_line(filelist):
    '''
    Gets a random non commented line from the file as a string
    and returns it as a list of charachters.
    '''
    line_list = []
    while not line_list: #make sure not to get an empty line
        try: #in case its zero
            random_num = random.randint(0, len(filelist) - 1)
        except ValueError:
            random_num = 0
        if (not filelist[random_num].strip().startswith('#') and
            not filelist[random_num].strip().startswith("'''") and
            not filelist[random_num].strip().startswith('"""')):
            line_list = list(filelist[random_num])
    return random_num, line_list


def single_char_swap(filelist, num_bugs, char1, char2):
    '''
    Randomly swaps two supplied charachters for each other.
    '''
    mylist = []
    random_num, mylist = random_line(filelist)
    mylist = filelist[random_num].split(' ')
    for x in range(len(mylist)):
        randomizer = random.randint(0,1)   #not too many on same line
        if randomizer:
            if char1 in mylist[x]:
                mylist[x] = mylist[x].replace(char1, char2)
                num_bugs -=1
                break
            elif char2 in mylist[x]:
                mylist[x] = mylist[x].replace(char2, char1)
                num_bugs -=1
                break
            else:
                continue
        elif randomizer == 0:
            continue        
    filelist[random_num] = ' '.join(mylist)
    return filelist, num_bugs

def tabs_spaces(filelist, num_bugs):
    '''
    Randomly adds or subtracts a space in a tabbed line,
    or adds a tab or double tab where it doesn't belong.
    '''
    mylist = []
    random_num, mylist = random_line(filelist)
    flag = random.randint(0,1)
    if mylist[:4] == [' ', ' ', ' ', ' ']:
        if flag:
            mylist.insert(0, ' ')
        else:
            del mylist[0]
    elif flag:
        for x in range(4):
            mylist.insert(0, ' ')
    else:
        for x in range(8):
            mylist.insert(0, ' ')

    num_bugs -=1                      
    filelist[random_num] = ''.join(mylist)
    return filelist, num_bugs

def num_change(filelist, num_bugs):
    '''
    Randomly adds or subtracts an int by 1.
    '''
    mylist = []
    random_num, mylist = random_line(filelist)
    for x in range(len(mylist)):
        randomizer = random.randint(0,2)
        if mylist[x].isdigit() and randomizer != 2:
            mylist[x] = int(mylist[x])
            if randomizer:
                mylist[x] += 1
            elif randomizer == 0:
                mylist[x] -= 1
            num_bugs -= 1
            mylist[x] = str(mylist[x])
            break
        else:
            continue
    filelist[random_num] = ''.join(mylist)
    return filelist, num_bugs


def period_swap(filelist, num_bugs):
    '''
    Randomly change period to a comma and vice versae.
    '''
    new_filelist, num_bugs_update = single_char_swap(filelist, num_bugs, ',', '.')
    return new_filelist, num_bugs_update
    

def zero_o(filelist, num_bugs):
    '''
    Randomly change 'o' to a Zero and vice versae.
    '''
    new_filelist, num_bugs_update = single_char_swap(filelist, num_bugs, 'o', '0')
    return new_filelist, num_bugs_update

def elif_else(filelist, num_bugs):
    '''
    Randomly change 'elif' to 'else' and vice versae.
    '''
    new_filelist, num_bugs_update = single_char_swap(filelist, num_bugs, 'elif', 'else')
    return new_filelist, num_bugs_update

def parentheses(filelist, num_bugs):
    '''
    Randomly changes brackets, parentheses and curly braces.
    '''
    bracks_open = ['(','{','[',':',]
    bracks_closed = [')','}',']',';',':']
    randomizer = random.randint(0,1)
    if randomizer:
        new_filelist, num_bugs_update = single_char_swap(filelist, num_bugs,random.choice(bracks_open), random.choice(bracks_open))
    else:
        new_filelist, num_bugs_update = single_char_swap(filelist, num_bugs,random.choice(bracks_closed), random.choice(bracks_closed))

    return new_filelist, num_bugs_update

def bugged_comment(filelist, num_bugs):
    '''
    Replaces comment with a specified comment.
    '''
    bug_comment = '#THIS COMMENT HAS BEEN BUGGIFIED!'
    flag = True
    while flag:
        for line in range(len(filelist)):
            #Sometimes this function will buggify a buggified docstring. need to review
            if filelist[line].strip().startswith('#') and random.randint(1, 5) == 1:
                filelist[line] = bug_comment
                flag = False
                num_bugs -= 1
                break
            else:
                continue
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
    Randomly switch a charachter with the one before it.
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

    

#List of all the bugs which buggify randomly chooses from to implement.    
function_list = [
                 zero_o,
                 parentheses,
                 bugged_comment,
                 bugged_docstring,
                 period_swap,
                 tabs_spaces,
                 num_change,
                 elif_else,
                 line_switch,
                 char_switch,
                 case_switch,
                 ]
