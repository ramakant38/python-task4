# Assignment 1
- using 'with' keyword and open() function specify the directory where 'sample.txt' file is present and use mode 'r' to read the file.

- then store the directory path get through open() function, in a variable 'file1'
- manually add some text to the sample.txt file.
- then using read() function access the content of the file and store in a variable 'readfile'.
- the print the content in terminal using print() function.
- then close the file using close() function
- All these code store in 'try:' block to check sample.txt file is present in the directory or not.
- if not present try block will raise the 'FileNotFound' error and to handdle the error use the 'except:' block.


# Assignment 2
- use open() function specify the directory where 'output.txt' file is present and use mode 'w' to write some text in the file.
- store the directory path in a variable 'file'
- take some text as input from keyboard and store in a variable 'text'
- then using write() function and passing 'text' variable as argument, to write the input text in the output.txt file.
- then close the file using close() function
- Again get the file directory path using open() and store in a variable 'file1' and use file mode 'a' to append additional text to the output.txt file.

- take some input from keyboard and store in a variable add.
- then use write() function and pass add variable as argument to append the content in the file.
- then close the file using close()

- Again get the file directory path using open() and store in a variable 'file2' and use file mode 'r' to read text to the output.txt file.
- then using read() fetch the content from the file and store in a variable 'getRead'
- the print the variable 'getRead' using print() in the terminal
- then close the file using close()