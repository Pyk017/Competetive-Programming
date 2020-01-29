string = input("Enter a string !")
sub_string = input("Enter a Sub-string !")
a = 0
for i in range(0, len(string)-len(sub_string)+1 ):
    if sub_string in string[i:len(sub_string)+i]:
        a = a + 1

print (a)
