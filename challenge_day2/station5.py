import pandas as pd
def solution_station_5(input):
    people = pd.read_csv('challenge_day2/people.csv')
    people = people.values.tolist()
    names = []
    teams = []
    j = 0
    for i in people:
        if j%2 != 0:
            teams.append(i)
        else:
            i = i[0]
            i = i.split(" ")[0]
            names.append(i)  
        j+=1
    print(input)
    print(type(input))
    index = names.index(input)
    team = teams[index][-1][-1]
    return team
