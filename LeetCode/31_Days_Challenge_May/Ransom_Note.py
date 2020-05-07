from collections import Counter

def canConstruct(ransom, magazine):
    c = dict(Counter(ransom))
        d = dict(Counter(magazine))
        for i in ransomNote:
            if i not in d or c[i] > d[i]:
                return False
            
        return True
        
ransomNote = input()
magazine = input()
print(canConstruct(ransomNote, magazine))
