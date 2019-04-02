import shutil, os, difflib, sys, random
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
from tkinter import messagebox
import argparse

class colors:
    '''Holds the color values that are put in when text is printed to the command line'''
    #Usage: print(colors.blue + "Hello there this is blue" + colors.endcolor)
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warning = '\033[93m'
    endcolor = '\033[0m'
    bold = '\033[1m'

class BuggifyGUI:

    def __init__(self):
        #Root configs
        self.root = Tk()
        self.root.title("Buggify")
        self.root.geometry("650x550")
        self.root.config(bg="lightblue")

        #Int variables for each of the bugs
        self.period_switch_int = IntVar()
        self.zero_o_switch_int = IntVar()
        self.elif_else_switch_int = IntVar()
        self.add_subtract_switch_int = IntVar()
        self.single_bracket_switch_int = IntVar()
        self.all_bracket_switch1_int = IntVar()
        self.all_bracket_switch2_int = IntVar()
        self.all_bracket_switch3_int = IntVar()
        self.line_switch_int = IntVar()
        self.char_switch_int = IntVar()
        self.case_switch_int = IntVar()
        self.equal_switch_int = IntVar()
        self.if_switch_int = IntVar()
        self.camel_snake_case_int = IntVar()
        self.tabs_spaces_int = IntVar()
        self.num_change_int = IntVar()
        self.missing_blanks_int = IntVar()
        self.scrambled_line_int = IntVar()
        self.bugged_comment_int = IntVar()
        self.bugged_docstring_int = IntVar()
        self.all_check_int = IntVar()
        self.bug_entry_var = StringVar()
        #Entry that the user can put in the number of bugs that they want in the program
        self.bugs_entry = Entry(self.root, textvariable=self.bug_entry_var, text="Number of Bugs")
        self.bugs_entry.grid(row=1, column=3)
        #Values get returned as 1 or 0, 1=checked and zero=!checked
        #Checkbutton(master, text="male", variable=var1).grid(row=0, sticky=W)
        Checkbutton(self.root, text="Period Switch", variable=self.period_switch_int, bg="lightblue", fg="black").grid(row=0, sticky=W)
        Checkbutton(self.root, text="Zero Switch", variable=self.zero_o_switch_int, bg="lightblue", fg="black").grid(row=1, sticky=W)
        Checkbutton(self.root, text="Elif Else Switch", variable=self.elif_else_switch_int, bg="lightblue", fg="black").grid(row=2, sticky=W)
        Checkbutton(self.root, text="Add/Subtract Switch", variable=self.add_subtract_switch_int, bg="lightblue", fg="black").grid(row=3, sticky=W)
        Checkbutton(self.root, text="Single Bracket Switch", variable=self.single_bracket_switch_int, bg="lightblue", fg="black").grid(row=4, sticky=W)
        Checkbutton(self.root, text="All Bracket Switch 1", variable=self.all_bracket_switch1_int, bg="lightblue", fg="black").grid(row=5, sticky=W)
        Checkbutton(self.root, text="All Bracket Switch 2", variable=self.all_bracket_switch2_int, bg="lightblue", fg="black").grid(row=6, sticky=W)
        Checkbutton(self.root, text="All Bracket Switch 3", variable=self.all_bracket_switch3_int, bg="lightblue", fg="black").grid(row=7, sticky=W)
        Checkbutton(self.root, text="Line Switch", variable=self.line_switch_int, bg="lightblue", fg="black").grid(row=8, sticky=W)
        Checkbutton(self.root, text="Char Switch", variable=self.char_switch_int, bg="lightblue", fg="black").grid(row=9, sticky=W)
        Checkbutton(self.root, text="Case Switch", variable=self.case_switch_int, bg="lightblue", fg="black").grid(row=10, sticky=W)
        Checkbutton(self.root, text="Equal Switch", variable=self.equal_switch_int, bg="lightblue", fg="black").grid(row=11, sticky=W)
        Checkbutton(self.root, text="If Switch", variable=self.if_switch_int, bg="lightblue", fg="black").grid(row=12, sticky=W)
        Checkbutton(self.root, text="Camel Snake Case", variable=self.camel_snake_case_int, bg="lightblue", fg="black").grid(row=13, sticky=W)
        Checkbutton(self.root, text="Tabs/Spaces Bug", variable=self.tabs_spaces_int, bg="lightblue", fg="black").grid(row=14, sticky=W)
        Checkbutton(self.root, text="Number Change", variable=self.num_change_int, bg="lightblue", fg="black").grid(row=15, sticky=W)
        Checkbutton(self.root, text="Missing Blanks", variable=self.missing_blanks_int, bg="lightblue", fg="black").grid(row=16, sticky=W)
        Checkbutton(self.root, text="Scrambled Line", variable=self.scrambled_line_int, bg="lightblue", fg="black").grid(row=17, sticky=W)
        Checkbutton(self.root, text="Bugged Comment", variable=self.bugged_comment_int, bg="lightblue", fg="black").grid(row=18, sticky=W)
        Checkbutton(self.root, text="Bugged Docstring", variable=self.bugged_docstring_int, bg="lightblue", fg="black").grid(row=19, sticky=W)
        Checkbutton(self.root, text="All Bugs", variable=self.all_check_int, bg="lightblue", fg="black").grid(row=20, stick=W)
        #buttons
        self.submit_button = Button(self.root, text="Submit", command=self.submit, bg="lightblue", fg="black").grid(row=20, column=3)
        self.file_select = Button(self.root, text="Select a file", command=self.file_select, bg="lightblue", fg="black").grid(row=8, column=3)
        #Labels
        self.main_label = Label(self.root, text="Buggify", bg="lightblue", fg="black")
        self.main_label.grid(row=0, column=3)

        #Main loop
        self.root.mainloop()

    def submit(self):
        '''Takes the values of the checkboxes and converts it into a list of the specified bugs the user wants'''
        buglist = []

        if self.period_switch_int == 1:
            buglist.append("ps")
        else:
            pass
        if self.zero_o_switch_int == 1:
            buglist.append("zs")
        else:
            pass
        if self.elif_else_switch_int == 1:
            buglist.append("ees")
        else:
            pass
        if self.add_subtract_switch_int == 1:
            buglist.append("addsubs")
        else:
            pass
        if self.single_bracket_switch_int == 1:
            buglist.append("sbs")
        else:
            pass
        if self.all_bracket_switch1_int == 1:
            buglist.append("abs1")
        else:
            pass
        if self.all_bracket_switch2_int == 1:
            buglist.append("abs2")
        else:
            pass
        if self.all_bracket_switch3_int == 1:
            buglist.append("abs3")
        else:
            pass
        if self.line_switch_int == 1:
            buglist.append("ls")
        else:
            pass
        if self.char_switch_int == 1:
            buglist.append("chars")
        else:
            pass
        if self.case_switch_int == 1:
            buglist.append("cases")
        else:
            pass
        if self.equal_switch_int == 1:
            buglist.append("eqs")
        else:
            pass
        if self.if_switch_int == 1:
            buglist.append("ifs")
        else:
            pass
        if self.camel_snake_case_int == 1:
            buglist.append("csc")
        else:
            pass
        if self.tabs_spaces_int == 1:
            buglist.append("ts")
        else:
            pass
        if self.num_change_int == 1:
            buglist.append("numc")
        else:
            pass
        if self.missing_blanks_int == 1:
            buglist.append("mb")
        else:
            pass
        if self.scrambled_line_int == 1:
            buglist.append("scl")
        else:
            pass
        if self.bugged_comment_int == 1:
            buglist.append("buggedc")
        else:
            pass
        if self.bugged_docstring_int == 1:
            buglist.append("buggeddoc")
        else:
            pass

        #If the all of the possible values are in the list, then just leave it, if they are not but all checkbox is selected
        #then the buglist value is all

        if self.all_check_int == 1:
            if len(buglist) == 20:
                pass
            else:
                buglist = ["all"]
        else:
            pass


        #After all the values have been put into the buglist, then that list is passed into the __init__ method in the class
        b = Buggify(bug_function_list=buglist)
        #Then, the program is run normally using the buggify method of the Buggify Class
        try:
            b.buggify(num_bugs=int(self.bugs_entry.get()), full_file_path=self.file)
        except ValueError:
            messagebox.showinfo("Error", "Please Enter the number of bugs!")

        #Remove the filepath label
        self.file_name_label.grid_forget()

    def file_select(self):
        '''Allows the user to select a file from the computer to "buggify", it then displays the path name in a label on the screen'''
        self.file = askopenfilename()
        self.main_label.grid_forget()
        self.file_name_label = Label(self.root, text="File To Buggify:" + str(self.file), fg="black", bg="lightblue", font=(10))
        #This grid is seperate because to remove the label by using grid_forget() method, the grid has to be seperate from the variable definition (Wierd Tk Requrinment)
        self.file_name_label.grid(row=0, column=3)
        return self.file


class CreateBugs:

    def __init__(self):
        #This list contains all the bugs which buggify() chooses from to implement.
        self.docstring_line_indexes = []
        self.bug_function_list = [
                    self.period_switch,
                    self.zero_o_switch,
                    self.elif_else_switch,
                    self.add_subtract_switch,
                    self.single_bracket_switch,
                    self.all_bracket_switch1,
                    self.all_bracket_switch2,
                    self.all_bracket_switch3,
                    self.line_switch,
                    self.char_switch,
                    self.case_switch,
                    self.equal_switch,
                    self.if_switch,
                    self.camel_snake_case,
                    self.tabs_spaces,
                    self.num_change,
                    self.missing_blanks,
                    self.scrambled_line,
                    self.bugged_comment,
                    self.bugged_docstring,
                    ]

####These first set of functions are used by the bug functions:
####random_line(), multi_char_switch(), all_char_switch() and docstring_detect()
        
    def random_line(self, filelist, opt_arg = 'line_list'):
        '''Gets a random line from the file as a string
        (as long as it's not a comment, part of a docstring,
        empty, the first line or the last line, or the second to last line)
        and returns it as a list of characters along with the chosen index.'''
        self.random_line_index = random.randint(0, len(filelist) - 1)
        if self.docstring_line_indexes == []:
            self.docstring_line_indexes = self.docstring_detect(filelist)

        while (filelist[self.random_line_index].strip().startswith('#') or
            self.random_line_index in self.docstring_line_indexes or
            len(set(filelist[self.random_line_index])) <= 2 or
            self.random_line_index >= (len(filelist) - 1) or
            self.random_line_index == 0):

            self.random_line_index = random.randint(0, len(filelist) - 1)
        
        if opt_arg == 'line_list':
            line_list = list(filelist[self.random_line_index])
            return self.random_line_index, line_list 
        return self.random_line_index

    def multi_char_switch(self, filelist, num_bugs, chars1, chars2, func_name=''):
        '''
        Switches two supplied characters or words for each other once in a line.
        They do not have to be the same length.
        '''
        line_index, line_char_list = self.random_line(filelist)
        
        #line_char_list must contain at least either chars1 or char2
        #Break the loop if it tries more than 100 times to prevent
        #a situation where the word or character isn't present in the file.
        #If a line can't be found, then that function is removed from the main
        #bug_function_list to ensure it isn't run again.
        line_search_tries = 100
        while chars1 not in filelist[line_index] or chars2 not in filelist[line_index]:
            line_index, line_char_list = self.random_line(filelist)
            line_search_tries -= 1
            if line_search_tries == 0:
                if func_name != '':
                    self.bug_function_list.remove(func_name)
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

    def all_char_switch(self, filelist, num_bugs, char1, char2, char3 = '', char4 = '', func_name = ''):
        '''
        Randomly changes all instances of a character in a line with another one.
        Optional: supply two additional characters for switching in a line.
        '''
        char_list = [char1, char2, char3, char4]
        line_index, line_char_list = self.random_line(filelist)  
        #line_char_list must contain at least one character from char_list
        #Break the loop if it tries more than 50 times to prevent
        #a situation where the characters aren't present in the file.
        #If a line can't be found, then the function is removed from the main
        #bug_function_list to ensure it isn't run again.
        line_search_tries = 100
        while not any(char in char_list for char in line_char_list):
            line_index, line_char_list = self.random_line(filelist)
            line_search_tries -= 1
            if line_search_tries == 0:
                if func_name != '':
                    self.bug_function_list.remove(func_name)
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

    def docstring_detect(self, filelist, return_start_end = 'no'):
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

        if self.docstring_line_indexes == []:
            self.docstring_line_indexes = full_doc_list

        if return_start_end == 'yes':
            return start_quotes, end_quotes
            
        return full_doc_list 

####These second set of functions are the bug functions themselves.

    def period_switch(self, filelist, num_bugs):
        '''
        Randomly switch period to a comma and vice versae.
        '''
        new_filelist, num_bugs_update = self.multi_char_switch(filelist=filelist, num_bugs=num_bugs, chars1=',', chars2='.', func_name=self.period_switch)
        return new_filelist, num_bugs_update
        
    def zero_o_switch(self, filelist, num_bugs):
        '''
        Randomly switch 'o' to a Zero and vice versae.
        '''
        new_filelist, num_bugs_update = self.multi_char_switch(filelist=filelist, num_bugs=num_bugs, chars1='o', chars2='0', func_name=self.zero_o_switch)
        return new_filelist, num_bugs_update

    def elif_else_switch(self, filelist, num_bugs):
        '''
        Randomly switch 'elif' to 'else' and vice versae.
        '''
        new_filelist, num_bugs_update = self.multi_char_switch(filelist=filelist, num_bugs=num_bugs, chars1='elif', chars2='else', func_name=self.elif_else_switch)
        return new_filelist, num_bugs_update

    def add_subtract_switch(self, filelist, num_bugs):
        '''
        Randomly switch '-' to '+' and vice versa.
        '''
        new_filelist, num_bugs_update = self.multi_char_switch(filelist=filelist, num_bugs=num_bugs, chars1='+', chars2='-', func_name=self.add_subtract_switch)
        return new_filelist, num_bugs_update

    def single_bracket_switch(self, filelist, num_bugs):
        '''Randomly switch one bracket type with another bracket type, returns the new_filelist and the new_bugs_update'''

        brackets = ['(','{','[',':',')','}',']',';',':']
        new_filelist, num_bugs_update = self.multi_char_switch(filelist=filelist, num_bugs=num_bugs,chars1=random.choice(brackets), chars2=random.choice(brackets), func_name=self.single_bracket_switch)
        return new_filelist, num_bugs_update

    def all_bracket_switch1(self, filelist, num_bugs):
        '''Switches all bracket types in a random line with another bracket type'''
        filelist, num_bugs = self.all_char_switch(filelist=filelist, num_bugs=num_bugs, char1='(', char2='[', char3=')', char4=']', func_name=self.all_bracket_switch1)
        return filelist, num_bugs

    def all_bracket_switch2(self, filelist, num_bugs):
        '''
        Switches all bracket types in a random line with another bracket type.
        '''
        filelist, num_bugs = self.all_char_switch(filelist=filelist, num_bugs=num_bugs, char1='(', char2='{', char3=')', char4='}', func_name=self.all_bracket_switch2)
        return filelist, num_bugs

    def all_bracket_switch3(self, filelist, num_bugs):
        '''
        Switches all bracket types in a random line with another bracket type.
        '''
        filelist, num_bugs = self.all_char_switch(filelist=filelist, num_bugs=num_bugs, char1='[', char2='{', char3=']', char4='}', func_name=self.all_bracket_switch3)
        return filelist, num_bugs

    def line_switch(self, filelist, num_bugs):
        '''
        Randomly switch a line with the one before it.
        '''   
        self.random_line_index = self.random_line(filelist, 'no_line_list')

        first_line = filelist[self.random_line_index]
        second_line = filelist[self.random_line_index - 1]
        
        filelist[self.random_line_index] = second_line
        filelist[self.random_line_index - 1] = first_line
        
        num_bugs -= 1
        return filelist, num_bugs

    def char_switch(self, filelist, num_bugs):
        '''
        Switch a randomly chosen character with the one before it,
        provided the character chosen isn't the first index
        and its previous character is not a white space.
        If a line is found with no consecutive characters,
        the while loop will be stuck trying to find a character
        whose previous character isn't a whitespace. After trying 50 times,
        it will simply switch the character with a white space and move on.
        '''
        line_index, line_char_list = self.random_line(filelist)
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
        
    def case_switch(self, filelist, num_bugs):
        '''
        Randomly switch the first character in a word from lower to upper and vice versae.
        '''
        num_times = num_bugs
        while num_times == num_bugs:
            line_index, line_char_list = self.random_line(filelist)
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

    def equal_switch(self, filelist, num_bugs):
        '''
        Switch '=' to '==' and vice versae
        '''
        line_index, line_char_list = self.random_line(filelist)
        line_search_tries = 100
        #If a line containing an '=' can't be found after 100 tries,
        #remove this function from the list so it can't be run again.
        while '=' not in line_char_list:
            line_index, line_char_list = self.random_line(filelist)
            line_search_tries -= 1
            if line_search_tries == 0:
                self.bug_function_list.remove(self.equal_switch)
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

    def if_switch(self, filelist, num_bugs):
        '''
        This function either:
        Removes an 'if' from the beginning of a line
        and the ':' from the end of a line,
        OR adds an 'if' to the beginning and ':' to the end of the line,
        and indents the following line with four additional spaces
        '''
        #Get random line index from the line
        #and doesn't return the line as a list of characters
        self.random_line_index = self.random_line(filelist, 'no_line_list')

        #Remove whitespaces from end of line to ensure that the ':' is the [-1] index.       
        filelist[self.random_line_index] = filelist[self.random_line_index].rstrip()

        #If 'if' is in the line and the last character is ':'
        #delete if, ':' and a whitespace character if that line is indented
        if filelist[self.random_line_index][-1] == ':':
            if 'if' in filelist[self.random_line_index] and 'elif' not in filelist[self.random_line_index]:
                if_index = filelist[self.random_line_index].index('if')
                line_list = list(filelist[self.random_line_index])
                del line_list[if_index + 1]
                del line_list[if_index]
                del line_list[-1]
                if line_list[0] == ' ':
                    del line_list[0]
                filelist[self.random_line_index] = ''.join(line_list)

        #If the last character is not a ':',
        #Add an 'if' after the initial whitespaces with a colon at the end.
        #Additionally, add four white spaces to the beginning of the next line
        elif filelist[self.random_line_index][-1] != ':' and filelist[self.random_line_index + 1] != '':
            line_list = list(filelist[self.random_line_index]) 
            for char_index in range(len(line_list)):
                if line_list[char_index] == ' ':
                    continue
                else:
                    line_list.insert(char_index, 'i')
                    line_list.insert(char_index + 1, 'f')
                    line_list.insert(char_index + 2, ' ')
                    line_list.append(':')
                    filelist[self.random_line_index] = ''.join(line_list)
                    break
            next_line_list = list(filelist[self.random_line_index + 1])
            for x in range(4):
                next_line_list.insert(0, ' ')
            filelist[self.random_line_index + 1] = ''.join(next_line_list)
            
        num_bugs -= 1
        return filelist, num_bugs

    def camel_snake_case(self, filelist, num_bugs):
        '''
        Converts snake_case to camelCase and vice versae.
        '''
        line_index, line_char_list = self.random_line(filelist)

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

    def tabs_spaces(self, filelist, num_bugs):
        '''
        Randomly adds or subtracts a space in a tabbed line,
        or adds a tab or double tab where it doesn't belong.
        '''
        line_index, line_char_list = self.random_line(filelist)
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

    def num_change(self, filelist, num_bugs):
        '''
        Randomly adds or subtracts an int by 1.
        '''
        line_index, line_char_list = self.random_line(filelist) 
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

    def missing_blanks(self, filelist, num_bugs):
        '''
        Replaces 1/3 of the non-whitespace characters in a line with underscores.
        
        Attempts to find a line with less than 5 underscores.
        If no such line is found after 20 tries, this function is removed from the list.
        Otherwise, the whole file becomes full of underscores
        when running this a large amount of times.
        '''
        line_index, line_char_list = self.random_line(filelist=filelist)
        line_search_tries = 20
        while line_char_list.count('_') > 5:
            line_index, line_char_list = self.random_line(filelist=filelist)
            line_search_tries -= 1
            if line_search_tries == 0:
                self.bug_function_list.remove(self.missing_blanks)
                return filelist, num_bugs

        spaceless_char_list = [index for index, value in enumerate(line_char_list) if value != ' ']
        for char in range(len(line_char_list) // 3):
            line_char_list[random.choice(spaceless_char_list)] = '_'
        filelist[line_index] = ''.join(line_char_list) + " #Fill in the missing blanks!"
        num_bugs -=1
        return filelist, num_bugs
        
    def scrambled_line(self, filelist, num_bugs):
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
        self.random_line_index = self.random_line(filelist, 'no_line_list')
        line_list = filelist[self.random_line_index].split()

        line_search_tries = 50
        while len(line_list) < 4:
            self.random_line_index = self.random_line(filelist, 'no_line_list')
            line_list = filelist[self.random_line_index].split()
            line_search_tries -= 1
            if line_search_tries == 0:
                self.bug_function_list.remove(self.scrambled_line)
                return filelist, num_bugs
            
        num_spaces = 0
        for char in filelist[self.random_line_index]:
            if char == ' ':
                num_spaces += 1
            else:
                break
        random.shuffle(line_list)
        filelist[self.random_line_index] = (num_spaces * ' ') + ' '.join(line_list) + " #Scrambled line!"
        num_bugs -=1
        return filelist, num_bugs
        
    def bugged_comment(self, filelist, num_bugs):
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

    def bugged_docstring(self, filelist, num_bugs):
        '''
        Replaces the lines of a random docstring with #BUGGIFIED DOCSTRING
        '''
        start_quotes, end_quotes = self.docstring_detect(filelist, return_start_end = 'yes')
        if start_quotes != [] or end_quotes != []:
            random_index = (random.randint(0, len(start_quotes))) - 1
            for docstring_line in range(start_quotes[random_index], (end_quotes[random_index]) + 1):
                filelist[docstring_line] = '#BUGGIFIED DOCSTRING'.rjust(24)
            num_bugs -= 1
        return filelist, num_bugs


    def random_line(self, filelist, opt_arg = 'line_list'):
        '''Gets a random line from the file as a string
        (as long as it's not a comment, part of a docstring,
        empty, the first line or the last line, or the second to last line)
        and returns it as a list of characters along with the chosen index.'''
        self.random_line_index = random.randint(0, len(filelist) - 1)
        if self.docstring_line_indexes == []:
            self.docstring_line_indexes = self.docstring_detect(filelist)
        else:
            pass

        while (filelist[self.random_line_index].strip().startswith('#') or
            self.random_line_index in self.docstring_line_indexes or
            len(set(filelist[self.random_line_index])) <= 2 or
            self.random_line_index >= (len(filelist) - 1) or
            self.random_line_index == 0):

            self.random_line_index = random.randint(0, len(filelist) - 1)
        
        if opt_arg == 'line_list':
            line_list = list(filelist[self.random_line_index])
            return self.random_line_index, line_list 

        return self.random_line_index

    def multi_char_switch(self, filelist, num_bugs, chars1, chars2, func_name=''):
        '''Switches two supplied characters or words for each other once in a line.
        They do not have to be the same length.'''
        line_index, line_char_list = self.random_line(filelist)
        
        #line_char_list must contain at least either chars1 or char2
        #Break the loop if it tries more than 100 times to prevent
        #a situation where the word or character isn't present in the file.
        #If a line can't be found, then that function is removed from the main
        #bug_function_list to ensure it isn't run again.
        line_search_tries = 100
        while chars1 not in filelist[line_index] or chars2 not in filelist[line_index]:
            line_index, line_char_list = self.random_line(filelist)
            line_search_tries -= 1
            if line_search_tries == 0:
                if func_name != '':
                    self.bug_function_list.remove(func_name)
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

    def all_char_switch(self, filelist, num_bugs, char1, char2, char3 = '', char4 = '', func_name = ''):
        '''
        Randomly changes all instances of a character in a line with another one.
        Optional: supply two additional characters for switching in a line.
        '''
        char_list = [char1, char2, char3, char4]
        line_index, line_char_list = self.random_line(filelist)  
        #line_char_list must contain at least one character from char_list
        #Break the loop if it tries more than 50 times to prevent
        #a situation where the characters aren't present in the file.
        #If a line can't be found, then the function is removed from the main
        #bug_function_list to ensure it isn't run again.
        line_search_tries = 100
        while not any(char in char_list for char in line_char_list):
            line_index, line_char_list = self.random_line(filelist)
            line_search_tries -= 1
            if line_search_tries == 0:
                if func_name != '':
                    self.bug_function_list.remove(func_name)
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

    def docstring_detect(self, filelist, return_start_end = 'no'):
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

        if self.docstring_line_indexes == []:
            self.docstring_line_indexes = full_doc_list
            

################################
### Section 2 - File Manager ###
################################

    
class FileManager:
    '''The File Manager Class holds all of the methods that have to do with file creation and modification'''

    def copy_file(self, file):
        '''Returns the original file and a copy of the original ('filename.py')
        into the same directory: "filenameBUGGIFIED.py"'''
        buggified_file = self.alter_file_name(file, 'BUGGIFIED')
        shutil.copy(file, buggified_file)
        return file, buggified_file

    def alter_file_name(self, full_file_path, word_to_insert, opt_arg='same_ext'):
        '''Returns a filename with a word inserted between a filename and its extension. 
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

    def convert_to_list(self, file):
        '''Returns the file as a list with each value being a new line EX:["line1","line2"]'''
        with open(file, errors='ignore') as f:
            filelist = f.read().splitlines()
        return filelist

    def answer_key_generate(self, file, bugfile, answer_key_file_name):
        '''Returns a diff file between the original file and the buggified file which contains 
        the differences between the two files, this function returns the answers file
        file= the name of the file that we are trying to write to
        bugfile=
        answer_key_file_name= a string of the filename of the program
        '''

        with open(file, errors='ignore') as f1:
            f1_txt = f1.read().splitlines()
            with open(bugfile) as f2:
                f2_txt = f2.read().splitlines()
                #What is the type of diff?
                diff = difflib.unified_diff(
                    f1_txt,
                    f2_txt,
                    fromfile='f1.txt',
                    tofile='f2.txt',
                    n = 0,
                    )
        with open(answer_key_file_name,'w', errors='ignore') as f:
            for line in diff:
                f.write(line)
                f.write('\n')
        return answer_key_file_name


################################
##### Section 3 - Buggify ######
################################
    

class Buggify:
    '''The Buggify Class holds the main buggify method which runs the program, the __init__ method of Buggify sets up which bugs that the user 
    wants to apply, and it also creates the nesssisary instances of the FileManager and the CreateBugs classes'''

    def __init__(self, bug_function_list=[]):
        #creates the instances of the classes that we need in the buggify function
        self.create_bugs = CreateBugs()
        self.filemanager = FileManager()

        #This code runs through the list of arguments that is passed through, it converts the abbv version
        #to the full function list
        #I spacifically had it replace the value in the list so that we didn't have to work with more than
        #One list in the class
        if bug_function_list != []:
            self.bug_function_list = bug_function_list
            for n, bug in enumerate(bug_function_list):
                if bug == "ps":
                    self.bug_function_list[n] = self.create_bugs.period_switch
                elif bug == "zs":
                    self.bug_function_list[n] = self.create_bugs.zero_o_switch
                elif bug == "ees":
                    self.bug_function_list[n] = self.create_bugs.elif_else_switch
                elif bug == "addsubs":
                    self.bug_function_list[n] = self.create_bugs.add_subtract_switch
                elif bug == "sbs":
                    self.bug_function_list[n] = self.create_bugs.single_bracket_switch
                elif bug == "abs1":
                    self.bug_function_list[n] = self.create_bugs.all_bracket_switch1
                elif bug == "abs2":
                    self.bug_function_list[n] = self.create_bugs.all_bracket_switch2
                elif bug == "abs3":
                    self.bug_function_list[n] = self.create_bugs.all_bracket_switch3
                elif bug == "ls":
                    self.bug_function_list[n] = self.create_bugs.line_switch
                elif bug == "chars":
                    self.bug_function_list[n] = self.create_bugs.char_switch
                elif bug == "cases":
                    self.bug_function_list[n] = self.create_bugs.case_switch
                elif bug == "eqs":
                    self.bug_function_list[n] = self.create_bugs.equal_switch
                elif bug == "ifs":
                    self.bug_function_list[n] = self.create_bugs.if_switch
                elif bug == "csc":
                    self.bug_function_list[n] = self.create_bugs.camel_snake_case
                elif bug == "ts":
                    self.bug_function_list[n] = self.create_bugs.tabs_spaces
                elif bug == "numc":
                    self.bug_function_list[n] = self.create_bugs.num_change
                elif bug == "mb":
                    self.bug_function_list[n] = self.create_bugs.missing_blanks
                elif bug == "scl":
                    self.bug_function_list[n] = self.create_bugs.scrambled_line
                elif bug == "buggedc":
                    self.bug_function_list[n] = self.create_bugs.bugged_comment
                elif bug == "buggeddoc":
                    self.bug_function_list[n] = self.create_bugs.bugged_docstring
                elif bug == "all":
                    self.bug_function_list = self.create_bugs.bug_function_list
                else:
                    print("Error")
        else:
            self.bug_function_list = self.create_bugs.bug_function_list

    def buggify(self, num_bugs=20, full_file_path=''):
        '''
        Main Buggify function.
        1. Creates copy of file and alters the filename
        2. Runs random bug functions to add errors into the copy of the file
        3. Outputs the answer key diff showing the bugs that were introduced

        Optional Arguments:
        num_bugs: int -- The amount of bugs to introduce. Defaults to 20 if left blank.
        full_file_path: string -- The FULL file path of the file to buggify. User May leave blank to be prompted to choose file
        '''

        #Code Below is used for the GUI in case the entry had no value (Probably won't happen because you would get an error from tk before this)
        if num_bugs == None or '':
            num_bugs = 20
        else:
            pass
            
        #If no file has been specified, it Removes small Tk window and prompts user to choose file.
        if full_file_path == '':
            Tk().withdraw()
            full_file_path = askopenfilename()

        #Reject files that are too small (only a few lines) or too big,
        #as they produce a wide variety of errors.
        filesize = os.path.getsize(full_file_path)
        #Detects the language of the file being Buggified
        self.language = self.detect_language(full_file_path)
        if filesize < 100 or filesize > 3000000:
            if filesize < 100:
                print("Failed to Buggify: " + full_file_path + "File is too small!")
            elif filesize > 3000000:
                print("Failed to Buggify: " + full_file_path + "\nFile is too big!")
            else:
                pass

        original_file, copy_of_file = self.filemanager.copy_file(full_file_path)   
        filelist = self.filemanager.convert_to_list(copy_of_file)
        #Answer key becomes a .txt file for easier reviewing
        answer_key_file_name = self.filemanager.alter_file_name(original_file, 'BUG-ANSWERKEY', 'text')

        #Main part of the program is run here, the while loop runs for the number of bugs in the program
        #This randomly selects one of the functions to run to create the bugs
        while num_bugs > 1:
            try:
                filelist, num_bugs = random.choice(self.bug_function_list)(filelist, num_bugs)
            except ValueError:
                print('WARNING! ValueError: buggify() may not have run successfully on ' + original_file)
                continue

        filechanges = '\n'.join(filelist)

        with open(copy_of_file, 'w', errors='ignore') as f:
            f.write(filechanges)

        self.filemanager.answer_key_generate(original_file, copy_of_file, answer_key_file_name)


    def detect_language(self, filename):
        '''Detects the language by checking the end of the filename'''
        if filename.endswith(".c"):
            return "c"
        elif filename.endswith(".py"):
            return "python"
        elif filename.endswith(".cpp"):
            return "c++"
        elif filename.endswith(".php"):
            return "php"
        elif filename.endswith(".html"):
            return "html"
        elif filename.endswith(".java"):
            return "java"
        elif filename.endswith(".js"):
            return "javascript"
        else:
            return "unknown language"

#Runs the program from the command line
if __name__ == "__main__":
    #Below uses the argparse module to manage the arguments
    parser = argparse.ArgumentParser(description='Buggify! Check the README.md for more information!')
    parser.add_argument("--numberofbugs", help="The number of bugs you want put in the script", type=int, default=20, required=False, nargs=1)
    parser.add_argument("--bugs", help="The specified bugs, see key in the README", default=[], nargs="*", required=False, choices=['ps','zs','ees','addsubs','sbs','abs','abs2','abs3','ls','chars','cases',
        'eqs','ifs','csc','ts','numc','mb','scl','buggedc','buggeddoc','all'])
    parser.add_argument("--scriptpath", help="Absolute path of the script to be 'Buggified'", default='', required=False, nargs=1, type=str)
    parser.add_argument("--GUI", help="Launch GUI Interface (usage: --GUI yes", nargs=1, default='no', required=False)
    args = parser.parse_args()

    #If the user did not specify the GUI, run the command line program, if they did, run the GUI

    if str(args.GUI).lower() == 'no':
        b = Buggify(bug_function_list=args.bugs)
        b.buggify(num_bugs=args.numberofbugs[0], full_file_path=args.scriptpath)
    else:
        print(colors.green + "Starting the GUI..." + colors.endcolor)
        gui = BuggifyGUI()

