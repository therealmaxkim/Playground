'''
Questions
1. Are the number of people on team 1 = # on team 2
2. Can a weight be missing or 0 from a team?

Observations
1. team 1 and team 2 are alternating
2. Go through array and add weight alternating


'''



def alternatingSums(a):
    team_1 = 0
    team_2 = 0 
    switch = True
    for i in range(len(a)):
        if switch:
            team_1 += a[i]
        else:
            team_2 += a[i]
        switch =  not switch
    
    return [team_1, team_2]