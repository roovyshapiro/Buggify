# Buggify
A Python Bugger which automatically inserts a random variety of syntax and logical errors into a program file. Buggify is a great tool for educational/training purposes, as well as interview and coding challenges.

Here's a basic overview of how the program works:

1. Choose a file and the number of bugs you'd like to introduce.
2. The file is copied to a new file with "BUGGIFIED" appended to the file name before the extension.
3. The number of bugs chosen acts as the range in a for loop
   which randomly calls on a list of bug functions to insert into the new copied file.
4. Once completed, a diff is stored showing the differences between the original and Buggified files.
5. The diff is stored as a new file and renamed with "BUG-ANSWERKEY" appended to the file name before the extension.