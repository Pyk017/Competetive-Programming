import string
special = string.punctuation
count = 0
s = input()
even = ''
odd = ''

for i in s:
    if i in special:
        count += 1
    if i in string.digits and int(i) % 2 == 0:
        even += i
    elif i in string.digits and int(i) % 2 != 0:
        odd += i
        
if count % 2 == 0:
    print(even + odd)
else:
    print(odd + even)