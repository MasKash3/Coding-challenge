#initializing
teams = []

matches = {}

# user inputs

# no of matches to limit the loop
no_matches = input("Enter number of matches: ")


for i in range(int(no_matches)):
    print(f"Match {i + 1}")
    first_team = input("Enter the first team: ")
    first_score = input("Enter the first team's score: ")
    second_team = input("Enter the second team: ")
    second_score = input("Enter the second's team score: ")
    print("<-------------------------------->")
# saves team name in a new variable that is going to be converted to a variable
    f_team_var = first_team
    s_team_var = second_team
# pass if the team was already added to the team list
    if first_team in teams:
        pass
    else:
# add team name to the team list and tp the match dictionary with an initial value of 0
        matches[f_team_var] = 0
        teams.append(first_team)
            
    if second_team in teams:
        pass
    else:
        teams.append(second_team)
        matches[s_team_var] = 0
        
# compare scores to add points
    if first_team in teams and second_team in teams:
        if first_score > second_score:
            matches[f_team_var] = matches[f_team_var] + 3
        elif first_score == second_score:
            matches[f_team_var] = matches[f_team_var] + 1
            matches[s_team_var] = matches[s_team_var] + 1
        elif first_score < second_score:
            matches[s_team_var] = matches[s_team_var] + 3

# print results
for k, v in matches.items():
    print("{}, {} pts".format(k, v))