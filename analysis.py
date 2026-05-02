import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")




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


print(deliveries.head())

top_batsmen = deliveries.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False)
print(top_batsmen.head(10))

sixes = deliveries[deliveries["batsman_runs"] == 6]
top_six_hitters = sixes["batter"].value_counts().head(5)
print(top_six_hitters)

fours = deliveries[deliveries["batsman_runs"] == 4]
top_four_hitters = fours["batter"].value_counts().head(5)
print(top_four_hitters)

# import matplotlib.pyplot as plt

top10 = top_batsmen.head(10)

plt.bar(top10.index, top10.values)
plt.xticks(rotation=45)
plt.title("Top 10 Batsmen by Runs")
plt.show()

merged = deliveries.merge(data, left_on="match_id", right_on="id")
winning_runs = merged[merged["winner"] == merged["team1"]]

top_winning_batsmen = winning_runs.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False)

print(top_winning_batsmen.head(10))

impact_players = merged["player_of_match"].value_counts().head(10)
print(impact_players)

print("\n=== MACHINE LEARNING SECTION ===\n")

ml_data = data[["team1", "team2", "toss_winner", "toss_decision", "venue", "winner"]].dropna()

# le = LabelEncoder()

# for col in ml_data.columns:
#     ml_data[col] = le.fit_transform(ml_data[col])

X = ml_data.drop("winner", axis=1)
y = ml_data["winner"]
X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)
print("Accuracy:", model.score(X_test, y_test))

sample = X_test.iloc[0].values.reshape(1, -1)
print("Predicted winner:", model.predict(sample))
