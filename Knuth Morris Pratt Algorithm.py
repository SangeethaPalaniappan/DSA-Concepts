# Knuth Morris Pratt Algorithm 
# (Prefix Sum)

string = "abcabdabcabeabcabdabcabc"
LPS = [0]
print(LPS)
for i in range(1, len(string)):
    x = LPS[i - 1]
    while string[i] != string[x]:
        if x != 0:
            x = LPS[x - 1]
        else:
            x = -1
            break
    
    LPS.append(x + 1)
print(LPS)    
        
    