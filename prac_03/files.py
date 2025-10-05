"""
CP1404/CP5632 - Practical
Files exercises
"""

#1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()


#2. In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
#Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
#Use open and close for this question.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")


# #3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result, which should be... 59. Use with instead of open and close for this question.





#4. Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers. Use with instead of open and close for this question.

