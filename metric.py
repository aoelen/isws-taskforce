###################
# Example of simple agreement between a list of voters,
# this could be in RDF, but currently it is just in a 
# python list
###################
votingData = [True, True, False, False]


'''def SimpleIIR(data):
    i = 0
    agreement = 0
    cases = 0
    while i < len(data):
        vote = data[i]
        j = i + 1
        while j < len(data):
            vote2 = data[j]
            cases += 1
            if (vote == vote2): 
                agreement += 1
            j+=1
        i+=1

    return agreement / cases'''

# same as SimpleIIR, but more clean code
def SimpleIIR2(data):
    from itertools import combinations
    combinations = combinations(data, 2)
    agreement = 0
    total = 0

    for combination in combinations:
        total += 1
        if (combination[0] == combination[1]):
            agreement += 1

    return agreement / total

def scoreIIR(agreement): 
    agreementLevel = ''

    if agreement >= 0 and agreement <= 0.20:
        agreementLevel = 'none'
    elif agreement >= 0.21 and agreement <= 0.39:
        agreementLevel = 'minimal'
    elif agreement >= 0.40 and agreement <= 0.59:
        agreementLevel = 'weak'
    elif agreement >= 0.60 and agreement <= 0.79:
        agreementLevel = 'moderate'
    elif agreement >= 0.80 and agreement <= 0.90:
        agreementLevel = 'strong'
    elif agreement >= 0.90 and agreement <= 1:
        agreementLevel = 'almost perfect'
    
    return agreementLevel


print('Simple inter-rater reliability, list:', votingData, ', agreement:', SimpleIIR2(votingData), ', so the agreement is:', scoreIIR(SimpleIIR2(votingData)))

###################
# Example of agreement between groups. First calculate agreement 
# per group. Then calculate total agreement. And see if there is 
# a difference, which is an indication for bias 
###################

def CalculateGroupDisagreement(groups):
    import numpy as np
    import itertools

    groupAgreements = [SimpleIIR2(group) for group in groups]

    averageGroupAgreement = np.mean(groupAgreements)
    print('average group agreement: ', averageGroupAgreement)

    agreementGroupsCombined = list(itertools.chain.from_iterable(groups)) # join all values from the arrays into one array
    groupIIR = SimpleIIR2(agreementGroupsCombined)

    print('total agreement all groups combined: ', groupIIR)

votingDataFR = [True, True, True, True]
votingDataPS = [False, False, False, False]
votingDataUS = [True, True, True, True]

groups = [votingDataFR, votingDataPS, votingDataUS] 

CalculateGroupDisagreement(groups)