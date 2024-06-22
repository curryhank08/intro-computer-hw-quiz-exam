# install pandas first using conda or pip
import pandas as pd

# Read the CSV file
df = pd.read_csv('/Users/yaohank/Library/CloudStorage/OneDrive-gs.ncku.edu.tw/計算機概論2/Exam/PE8/pe8_data.csv')

# debug
#print(df)
#print()

print("1.")
# 1. Identify Eastern Conference teams with a HOME win-loss percentage lower than their AWAY win-loss percentage.
eastern_teams = df[df['Conference'] == 'Eastern']
HOME_win_percentage = eastern_teams['HOME'].str.split('-').apply(lambda x: int(x[0]) / (int(x[0]) + int(x[1])))
AWAY_win_percentage = eastern_teams['AWAY'].str.split('-').apply(lambda x: int(x[0]) / (int(x[0]) + int(x[1])))

teams_with_lower_HOME_percentage = eastern_teams[HOME_win_percentage < AWAY_win_percentage]['Team']
print("Eastern Conference teams with a HOME win-loss percentage lower than AWAY win-loss percentage:")
for team in teams_with_lower_HOME_percentage:
    print(team)
print()

print("2.")
# 2. Determine which conference has a higher average difference about "PF minus PA".
df['PF_minus_PA'] = df['PF'] - df['PA']
conference_avg_difference = df.groupby('Conference')['PF_minus_PA'].mean()

higher_avg_difference_conference = conference_avg_difference.idxmax()
print(f"The conference with a higher average difference of PF minus PA is: {higher_avg_difference_conference}")

print()
print("3.")
# 3. Generate a ranking list of all teams based on their overall win percentage.
df['Wins'] = df['W-L'].str.split('-').apply(lambda x: int(x[0]))
df['Losses'] = df['W-L'].str.split('-').apply(lambda x: int(x[1]))
df['TotalGames'] = df['Wins'] + df['Losses']
df['Win_Percentage'] = df['Wins'] / df['TotalGames']

ranking = df.sort_values(by='Win_Percentage', ascending=False)[['Team', 'Win_Percentage']]
print("Ranking of teams based on overall win percentage:")
print(ranking)

''' Answer:
1.
Eastern Conference teams with a HOME win-loss percentage lower than AWAY win-loss percentage:
Knicks
Hornets

2.
The conference with a higher average difference of PF minus PA is: Eastern

3.
Ranking of teams based on overall win percentage:
             Team  Win_Percentage
0           Bucks        0.707317
1         Celtics        0.695122
2           76ers        0.658537
15        Nuggets        0.646341
3       Cavaliers        0.621951
16      Grizzlies        0.621951
17          Kings        0.585366
4          Knicks        0.573171
5            Nets        0.548780
18           Suns        0.548780
19       Clippers        0.536585
20       Warriors        0.536585
7            Heat        0.536585
21         Lakers        0.524390
23       Pelicans        0.512195
22   Timberwolves        0.512195
8         Raptors        0.500000
6           Hawks        0.500000
9           Bulls        0.487805
24        Thunder        0.487805
25      Mavericks        0.463415
26           Jazz        0.451220
11        Wizards        0.426829
10         Pacers        0.426829
12          Magic        0.414634
27  Trail Blazers        0.402439
13        Hornets        0.329268
28        Rockets        0.268293
29          Spurs        0.268293
14        Pistons        0.207317
'''