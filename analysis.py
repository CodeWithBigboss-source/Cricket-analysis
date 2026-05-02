import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("matches.csv")

print(data.head())
print(data.columns)
print(data.info())
print("Total matches:", len(data))
print(data["winner"].value_counts())
print(data["winner"].value_counts().head(5))
print(data["player_of_match"].value_counts().head(5))
matches_team1 = data["team1"].value_counts()
matches_team2 = data["team2"].value_counts()

total_matches = matches_team1 + matches_team2

print(total_matches.sort_values(ascending=False).head(10))
print(data["toss_winner"].value_counts().head(5))
toss_match = data[data["toss_winner"] == data["winner"]]
print("Times toss winner also won match:", len(toss_match))

mi_matches = total_matches["Mumbai Indians"]
mi_wins = data["winner"].value_counts()["Mumbai Indians"]
print("Matches:", mi_matches)
print("Wins:", mi_wins)
print("Win %:", (mi_wins / mi_matches) * 100)



top_teams = data["winner"].value_counts().head(5)

plt.bar(top_teams.index, top_teams.values)
plt.title("Top 5 Teams by Wins")
plt.xticks(rotation=45)
plt.show()

top_players = data["player_of_match"].value_counts().head(5)

plt.bar(top_players.index, top_players.values)
plt.title("Top Players (MOTM Awards)")
plt.xticks(rotation=45)
plt.show()