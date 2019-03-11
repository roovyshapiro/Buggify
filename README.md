# Buggify Overview
Buggify is a Python bugger which automatically inserts a random variety of syntax and logical errors into a program file. Buggify is a great tool for educational/training purposes, interview/coding challenges, or even as a way to prank your friends!


#### In this example, 
- Buggify.py is double clicked. 
- buggify_functions.py is chosen in the file prompt. 
- Two files are automatically generated:
    - buggify_functionsBUGGIFIED.py -> _The version of the file with all the bugs added to it._
    - buggify_functionsBUG-ANSWERKEY.py.txt -> _The answer key which contains a Diff between the two files showing what has changed._
___    
![](https://i.imgur.com/FGx906Z.gif)
___
# Buggify.py Overview
The main function that does all the work is buggify(). Here's how it works:
~~~~
buggify(num_bugs, file)
~~~~
 1. Specify the number of bugs you'd like to introduce and the file you'd like to apply the bugs to. If the number of bugs is left blank, it will default to 20. If the file isn't specified, the user will be prompted to choose one.  
 2. The file is copied to a new file with "BUGGIFIED" appended to the file name but before the extension. This ensures that no changes will be made to the original file.
 3. buggify() calls on **bug_function_list** which is a global list in buggify_functions.py that stores all the different bug functions. Num_bugs acts as a range in a foor loop and each time buggify() chooses one function at random from this list to insert into the new copied file.
 4. Once completed, a diff is stored as a new text file showing the differences between the original and Buggified files. The diff is renamed with "BUG-ANSWERKEY" appended to the file name.

# buggify_functions.py Overview
The primary purpose of this file is the global list variable, **bug_function_list**.
The buggify() function in Buggify.py chooses functions at random from this list in order to affect the buggified file.

This file can be split up into three sections.
1. Helper Functions - Functions that are used by other functions. 
2. Bug Functions - The functions that are present in bug_function_list which actually apply the bugs.
3. Global Variables.



## Implemented Bug functions in bug_function_list

*(Typically, only one bug is implemented per line chosen at random. However, examples may show more than one bug per line for the sake of clarity.)*

 - **period_switch()**
	 - Switches a period to a comma and vice versa.
	 ~~~~
	 - line_char_list.insert(char_index + 1, '=')
	 ~~~~ 
	 ~~~~
	 + line_char_list,insert(char_index + 1. '=')
	 ~~~~ 
	 
 - **zero_o_switch()**
	 - Switches a zero to a lower case 'o' and vice versa.
	 ~~~~
	 - random_index = random.randint(0, len(line_char_list) - 1)
         + random_index = rand0m.randint(o, len(line_char_list) - 1)
	 ~~~~
	 
 - **elif_else_switch()**
	 - Switches "else" to "elif" and vice versa.
	 ~~~~
	  if randomizer == 0:
              line_char_list.insert(0, ' ')
         - elif randomizer == 1:
              del line_char_list[0]
         - else randomizer == 2:
	 ~~~~
	 ~~~~
	  if randomizer == 0:
              line_char_list.insert(0, ' ')
         + else randomizer == 1:
              del line_char_list[0]
         + elif randomizer == 2:
	 ~~~~
	 
 - **add_subtract_switch()**
	 - Switches a '+' to a '-' and vice versa.
	 ~~~~
	 - line_char_list[char_index - 1] not in ['=','!','+','-'] and
	 ~~~~ 
	 ~~~~
	 + line_char_list[char_index + 1] not in ['=','!','-','+'] and
	 ~~~~ 
	 
 - **single_bracket_switch()**
	- A bracket character is changed with another bracket type character once per line.
	 ~~~~
	 - if filelist[line_index][hash_index - 1].isspace() and random.randint(1, 3) == 1:
         + if filelist{line_index)[hash_index - 1).isspace(] and random.randint{1, 3] == 1;
	 ~~~~
	 
 - **all_bracket_switch1()**
 	- All parentheses found in a line are switched with square brackets and vice versa.
	~~~~
	- if filelist[line_index][hash_index - 1].isspace() and random.randint(1, 3) == 1:
	+ if filelist(line_index)(hash_index - 1).isspace[] and random.randint[1, 3] == 1:
	~~~~
	~~~~
	- random_index = random.randint(0, len(line_char_list) - 1)
	+ random_index = random.randint[0, len[line_char_list] - 1]
	~~~~
	
 - **all_bracket_switch2()**
 	- All parentheses found in a line are switched with curly brackes and vice versa.
	~~~~
	- if filelist[line_index][hash_index - 1].isspace() and random.randint(1, 3) == 1:
	+ if filelist[line_index][hash_index - 1].isspace{} and random.randint{1, 3} == 1:
	~~~~
	~~~~
	- random_index = random.randint(0, len(line_char_list) - 1)
	+ random_index = random.randint{0, len{line_char_list} - 1}
	~~~~
	
 - **all_bracket_switch3()**
 	- All square backets found in a line are switched with curly braces and vice versa.
	~~~~
	- if filelist[line_index][hash_index - 1].isspace() and random.randint(1, 3) == 1:
	+ if filelist{line_index}{hash_index - 1}.isspace() and random.randint(1, 3) == 1:
	~~~~
	~~~~
	- [num for num in doc_list if doc_list.index(num) % 2 == 0]
	+ {num for num in doc_list if doc_list.index(num) % 2 == 0}
	~~~~
	
 - **line_switch()**
	 - Switches a full line with the line before it.
	 ~~~~
	  line_char_list[x] = line_char_list[x].replace(char1, char2)
         - num_bugs -=1
         - break
	 ~~~~
	 ~~~~
	 line_char_list[x] = line_char_list[x].replace(char1, char2)
         + break
         + num_bugs -=1
	 ~~~~
	 
 - **char_switch()**
 	- Switches a character with the one before it.
	~~~~	    
    - return new_filelist, num_bugs_update
	~~~~	
	~~~~	    
    + return new_filelsit, num_bugs_update
    	~~~~

 - **case_switch()**
	 - Switches the first character in a word from lower case to upper case and vice versa.
	 ~~~~
	 - random_line_index = Random_line(filelist, 'no_line_list')
	 ~~~~
	 ~~~~
	 - Random_line_index = random_line(filelist, 'no_line_list')
	 ~~~~

 - **equal_switch()**
	 - Switches a double equals sign '==' to a single equals sign '=' and vice versa.
	 ~~~~
	 - start_quotes = [x for x in doc_list if doc_list.index(x) % 2 == 0]
	 ~~~~
	 ~~~~
	 + start_quotes == [x for x in doc_list if doc_list.index(x) % 2 = 0]
	 ~~~~

 - **if_switch()**
	 - Option #1:
		 - Removes the 'if' from the beginning of a line and the ':' from the end of a line.
		 ~~~~
		-  if line_char_list[char_index] == 0:
                	line_char_list[char_index] += 1
		 ~~~~
		 ~~~~
		 +  line_char_list[char_index] == 0
                    line_char_list[char_index] += 1
		 ~~~~
	    - Option #2: 
		    - Adds an 'if' to the beginning of the line and a ':' to the end of the line. 
		      Additionally, the following line is indented with four additional spaces.
		    ~~~~
		    - first_line = filelist[random_line_index]
		    - second_line = filelist[random_line_index - 1]
		    ~~~~
		    ~~~~
		    + if first_line = filelist[random_line_index]:
		    +     second_line = filelist[random_line_index - 1]
		    ~~~~

 - **camel_snake_case()**
	 - Switches a phrase written in snake_case to camelCase and vice versa.
	 ~~~~
	 - line_char_list = filelist[lineIndex].split(' ')
	 ~~~~
	 ~~~~
	 + lineCharList = filelist[line_index].split(' ')
	 ~~~~
	 
 - **tabs_spaces()**
	 - Option #1:
		 - Four spaces in the beginning of a line are increased by 1.
		 ~~~~
		 -    line_list = list(filelist[random_line_index])
		 +     line_list = list(filelist[random_line_index])
		 ~~~~
	 - Option #2:
		 - Four spaces in the beginning of a line are decreased by 1.
		 ~~~~
		 -    line_list = list(filelist[random_line_index])
		 +   line_list = list(filelist[random_line_index])
		 ~~~~ 
	 - Option #3:
		 - Four spaces in the beginning of a line are increased by 4 (a double tab).
		 ~~~~
		 -    line_list = list(filelist[random_line_index])
		 +        line_list = list(filelist[random_line_index])
		 ~~~~
	 - Option #4:
		 - A line which originally didn't have any spaces in the beginning has four spaces inserted at its beginning.
		 ~~~~
		 - def zero_o_switch(filelist, num_bugs):
		 +     def zero_o_switch(filelist, num_bugs):
		 ~~~~
		 
- **num_change()**
	 - An integer is either increased or decreased by 1.
	 ~~~~
	 - line_char_list[x] = line_char_list[x].replace(char2, char1)
	 ~~~~ 
	 ~~~~
	 + line_char_list[x] = line_char_list[x].replace(char1, char2)
	 ~~~~ 

- **missing_blanks()**
	 - One third of all non-white space characters in a random line	are replaced with underscores .
	   Appends "#Fill in the missing blanks!".
	 ~~~~
	 - while line_char_list.count('_') > 5:
	 ~~~~ 
	 ~~~~
	 + _hile _i_e__ha__list._ou_t_'_'_ > 5: #Fill in the missing blanks!
	 ~~~~ 
	 
- **scrambled_line()**
	 - Randomly rearranges all the words (defined as separated by whitespace) in a random line.
	   Appends "#Scrambled line!" to the end.
	 ~~~~
	 - for y in range(start_quotes[x], end_quotes[x] + 1):
	 ~~~~ 
	 ~~~~
	 + in y 1): for range(start_quotes[x], end_quotes[x] + #Scrambled line!
	 ~~~~

 - **bugged_comment()** 
	 - A comment beginning with a "#" is replaced with *#THIS COMMENT HAS BEEN BUGGIFIED*. 
	 While not a syntax or logical error *per se*, it does make the code more difficult to understand.  
	    ~~~~ 
          if full_file_path == '':
        - #Removes small Tk window and prompts user to choose file.
          Tk().withdraw()
	    ~~~~
	    ~~~~
	      if full_file_path == '':
        + #THIS COMMENT HAS BEEN BUGGIFIED
          Tk().withdraw()
	    ~~~~
	 
 - **bugged_docstring()**
	 - A full docstring is replaced with *#BUGGIFIED DOCSTRING*. 
	   This is similar to bugged_comment() in that its not a syntax or logical error *per se*, 
	   but it does make functions more difficult to understand.
	 ~~~~
	  def tabs_spaces(filelist, num_bugs):
         -    '''
         -    Randomly adds or subtracts a space in a tabbed line,
         -    or adds a tab or double tab where it doesn't belong.
         -    '''
	 ~~~~
	 ~~~~
	  def tabs_spaces(filelist, num_bugs):
         +    #BUGGIFIED DOCSTRING
         +    #BUGGIFIED DOCSTRING
         +    #BUGGIFIED DOCSTRING
         +    #BUGGIFIED DOCSTRING
	 ~~~~
