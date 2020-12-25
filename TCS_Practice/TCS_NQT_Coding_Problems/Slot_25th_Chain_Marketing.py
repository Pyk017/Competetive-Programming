parent = input()
status = input()
amt = 250
child = []
n = 0
if status == 'Y':
    amt = 0
    child = input().split()
    n = len(child)
    amt = n * 500

print("Total Members: {}".format(n + 1))
print("Comission Details")
print("{}: {} INR".format(parent, amt))
if status == "Y":
    for i in child:
        print("{}: 250 INR".format(i))
