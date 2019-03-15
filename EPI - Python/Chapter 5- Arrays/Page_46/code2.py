'''
Are the binary bits the same length?

A: #######
B:    ####

A:    ####
B: #######

A: #######
B: #######

'''
def add_two_bits(A, B):
    large = B if len(B) >= len(A) else A
    small = A if len(B) >= len(A) else B 

    #Add everything except the first number
    for i in reversed(range(1, len(small))):
        if large[i] + small[i] == 2: # 1 + 1 
            large[i] = 0
            large[i-1] += 1
        elif large[i] + small[i] == 3: # 1 + 1 + 1
            large[i] = 1
            large[i-1] += 1
        else:
            break

    #The A and B are not the same lengths, move up on the larger.
    for i in reversed(range(1, len(large)-len(small))):
        if large[i] == 2:
            large[i] = 0
            large[i-1] += 1
        else:
            break

    #Do the first element. Different outcome depending on same or different lengths
    if len(large) == len(small):
        if large[0] + small[0] == 2:
            large[0] = 0
            large.insert(0, 1)
        elif large[0] + small[0] == 3:
            large[0] = 1
            large.insert(0, 1)
    else:
        if large[0] == 2:
            large[0] = 0
            large.insert(0, 1)
        elif large[0] == 3:
            large[1] = 1
            large.insert(0, 1)
        
    return large


if __name__ == "__main__":
    print(add_two_bits([1, 0, 1], [1, 1, 1]))
