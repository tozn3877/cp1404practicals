"""
CP1404/CP5632 - Practical
Random numbers examples
"""

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


# What did you see on line 1?
#8
# What was the smallest number you could have seen, what was the largest?
#smallest number is 5 and largest is 20
# What did you see on line 2?
#3
# What was the smallest number you could have seen, what was the largest?
#smallest number would be 3 and largest would be 9
# Could line 2 have produced a 4?
#no
# What did you see on line 3?
#4.095198421386108
# What was the smallest number you could have seen, what was the largest?
#2.5
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))