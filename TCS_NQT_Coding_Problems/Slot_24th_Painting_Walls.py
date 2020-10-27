inter = int(input())
exter = int(input())
total_inter, total_exter = 0, 0

if inter == 0:
    total_inter = 0
else:
    for _ in range(inter):
        total_inter += float(input())
    total_inter *= 18

if exter == 0:
    total_exter = 0
else:
    for _ in range(exter):
        total_exter += float(input())
    total_exter *= 12
    

print("Total estimated Cost : {:.2f} INR".format(total_exter + total_inter))
    