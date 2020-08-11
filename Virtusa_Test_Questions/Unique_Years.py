# The UNO realease an official document regarding the most important event from the beginning of time (dated 00-00-0000) with a brief description 
# of the events. The date of all the events is mentioned in the "DD-MM-YYYY" format.

# Find the total number of distinct years referenced in the document.

# Input :
# input 1: String containing the content of the document.

# Output :
# Return the total number of distinct years referenced in the document

# Example 1:

# input 1: UN was established on 24-10-1945. India got freedom on 14-08-1947.and
# Output 1: 2

# Example 2:

# input 2: I was born on 25-07-1999. This date 25-07-1999 is special
# output 2: 1


import re
pattern = re.compile("-[0-9][0-9][0-9][0-9]*")
string = input()
res = pattern.findall(string)
print(set(res))
