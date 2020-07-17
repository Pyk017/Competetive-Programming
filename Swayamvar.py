def swayamvar(bride, groom):
    i, j = 0, 0
    while bride or groom:
        count = 0
        while bride[0] != groom[j] and count <= len(groom):
            j = (j + 1) % len(groom)
            count += 1
        
        if(count <= len(groom)):
            bride.pop(0)
            groom.pop(j)
            try:
                j = (j + 1) % len(groom)
            except:
                continue
        else:
            break
    
    print("bride : ", bride)
    print("groom : ", groom)
    return len(groom)
            
            


n = int(input())
Bride = input()
Groom = input()
res = swayamvar(list(Bride), list(Groom))
print(res)