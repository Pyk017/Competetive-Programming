# A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

# Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

# Example

# For inputString = "00-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = true;
# For inputString = "Z1-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = false;
# For inputString = "not a MAC-48 address", the output should be
# isMAC48Address(inputString) = false.


def isMAC48(inputString):
    if '-' not in inputString:
        return False
    
    ls = inputString.split('-')
    for i in ls:
        if (i[0] in '0123456789' or i[0] in 'ABCDEF') and (i[1] in '0123456789' or i[1] in 'ABCDEF'):
            flag = True
        else:
            flag = False
            break

    return True if flag else False


string = input()
print(isMAC48(string))