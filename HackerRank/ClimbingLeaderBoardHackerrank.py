def rank(score, alice):
    l = list(set(score))
    for i in range((len(alice))):
        l.append(alice[i])
        l = list(set(l))
        l = sorted(l, reverse = True)
        print (l.index(alice[i]) + 1)

score_count = int(input("Enter range of Score of LeaderBoard : "))
print("Enter Scores of LeaderBoard :- ")
score = list(map(int, input().rstrip().split()))
alice_count = int(input("Enter range of Score of Alice : "))
print("Enter Scores of Alice :- ")
alice = list(map(int, input().rstrip().split()))
rank(score, alice)

#Sample Inputs
#  7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120
