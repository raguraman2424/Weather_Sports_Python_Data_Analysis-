import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set_style("whitegrid")

# -----------------------------
# 🎯 Create Dataset
# -----------------------------
data = pd.DataFrame({
    "District": [
        "Chennai", "Coimbatore", "Madurai", "Salem", "Trichy",
        "Tirunelveli", "Erode", "Thanjavur", "Vellore", "Dindigul",
        "Namakkal", "Tiruppur", "Karur", "Kanyakumari", "Virudhunagar"
    ],
    "Sport": [
        "Cricket", "Football", "Running", "Kabaddi", "Carrom",
        "Cricket", "Football", "Running", "Kabaddi", "Carrom",
        "Cricket", "Football", "Running", "Kabaddi", "Carrom"
    ],
    "Participants": [120, 100, 80, 90, 60, 110, 95, 70, 85, 55, 100, 88, 65, 92, 50],
    "Winner": [
        "Chennai", "Coimbatore", "Madurai", "Trichy", "Salem",
        "Chennai", "Coimbatore", "Erode", "Vellore", "Madurai",
        "Namakkal", "Tiruppur", "Karur", "Kanyakumari", "Virudhunagar"
    ],
    "Runner": [
        "Madurai", "Erode", "Trichy", "Chennai", "Coimbatore",
        "Salem", "Vellore", "Thanjavur", "Dindigul", "Tirunelveli",
        "Tiruppur", "Namakkal", "Kanyakumari", "Virudhunagar", "Karur"
    ],
    "Prize (₹)": [50000, 40000, 30000, 35000, 20000, 48000, 42000, 31000, 37000, 25000, 46000, 41000, 32000, 36000, 23000]
})

print("🏅 Sample Data:\n", data.head())

# -----------------------------
# 📊 Summary Statistics
# -----------------------------
print("\n📈 Summary Statistics:")
print(data.describe())

# -----------------------------
# 🥇 Sport-wise total participants
# -----------------------------
plt.figure(figsize=(8,5))
sns.barplot(x="Sport", y="Participants", data=data, estimator=sum, palette="viridis")
plt.title("Total Participants per Sport")
plt.ylabel("Total Participants")
plt.show()

# -----------------------------
# 🏆 District-wise participation count
# -----------------------------
plt.figure(figsize=(10,5))
sns.barplot(x="District", y="Participants", data=data, palette="magma")
plt.title("District-wise Sports Participation")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 💰 Prize distribution by sport
# -----------------------------
plt.figure(figsize=(7,5))
sns.boxplot(x="Sport", y="Prize (₹)", data=data, palette="Set2")
plt.title("Prize Distribution by Sport")
plt.show()

# -----------------------------
# 📍 Winners by sport
# -----------------------------
winner_count = data.groupby("Winner")["Sport"].count().reset_index()
winner_count.rename(columns={"Sport": "Titles Won"}, inplace=True)

plt.figure(figsize=(8,5))
sns.barplot(x="Winner", y="Titles Won", data=winner_count, palette="coolwarm")
plt.title("Districts with Most Wins")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 🥈 Runner-up analysis
# -----------------------------
runner_count = data.groupby("Runner")["Sport"].count().reset_index()
runner_count.rename(columns={"Sport": "Runner-up Count"}, inplace=True)

plt.figure(figsize=(8,5))
sns.barplot(x="Runner", y="Runner-up Count", data=runner_count, palette="rocket")
plt.title("Districts with Most Runner-up Positions")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 🧠 Insights
# -----------------------------
print("\n🏁 Insights:")
top_winner = winner_count.loc[winner_count['Titles Won'].idxmax(), 'Winner']
top_participation = data.loc[data['Participants'].idxmax(), 'District']
print(f"🏆 Top Winning District: {top_winner}")
print(f"👥 Most Participants from: {top_participation}")
