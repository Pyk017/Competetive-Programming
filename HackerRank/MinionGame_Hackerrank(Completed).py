def consonant_list(string):
    l = []
    for i in string:
        if is_vowel(i):
            pass
        else:
            if i not in l:
                l.append(i)
    return l

def vowel_list(string):
    l = []
    for i in string:
        if is_vowel(i):
            if i not in l:
                l.append(i)
    return l

def is_vowel(letters):
    return letters in ['a','e','i','o','u','A','E','I','O','U']

def winner(x,y,name_1,name_2):
    if x > y:
        return "{} is Winner with score {}!".format(name_1,x)
    else:
        return "{} is Winner with score {}!".format(name_2,y)


string = input("The Game String will be :- ")
player_1 = input("Enter the name of first player :- ")
player_2 = input("Enter the name of second player :- ")

score_vowel,score_conso = 0,0
new_VowelList = vowel_list(string)
for j in new_VowelList:
    ind_v = list(string).index(j)
    for i in range(ind_v, len(string)):
        score_vowel = score_vowel + string.count(string[ind_v:i + 1])
        print(string[ind_v:i + 1])

print("Score for Player 1 is {}".format(score_vowel))

new_ConsonantList = consonant_list(string)
for j in new_ConsonantList:
    ind_c = list(string).index(j)
    for i in range(ind_c, len(string)):
        score_conso = score_conso + string.count(string[ind_c:i+1])
        print(string[ind_c:i + 1])

print("Score for Player 2 is {}".format(score_conso))

print(winner(score_conso,score_vowel,player_1,player_2))