import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

# --------------------------------
# 🌦 Create dataset
# --------------------------------
data = {
    "District": [
        "Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Tiruvannamalai",
        "Vellore", "Trichy", "Viluppuram", "Kanyakumari", "Krishnagiri", "Madurai",
        "Pudukkottai", "Salem", "Tenkasi", "Tiruppur", "Namakkal", "Nilgiris", "Kanchipuram"
    ],
    "Temperature(°C)": [33, 30, 32, 31, 29, 32, 30, 33, 31, 29, 30, 34, 31, 32, 28, 30, 31, 27, 33],
    "Humidity(%)": [70, 75, 72, 68, 73, 70, 69, 72, 71, 78, 70, 68, 74, 69, 76, 70, 71, 65, 70],
    "Pressure(hPa)": [1008, 1007, 1006, 1005, 1009, 1008, 1007, 1006, 1008, 1005, 1007, 1004, 1006, 1007, 1005, 1006, 1008, 1004, 1009],
    "WindSpeed(m/s)": [3.2, 3.5, 3.1, 2.9, 3.0, 3.3, 2.8, 3.2, 3.1, 2.7, 3.0, 3.4, 3.2, 3.3, 2.8, 3.0, 3.1, 2.5, 3.3],
    "Condition": [
        "Cloudy", "Rainy", "Humid", "Clear", "Rainy", "Cloudy", "Clear", "Sunny",
        "Humid", "Rainy", "Clear", "Sunny", "Cloudy", "Rainy", "Humid", "Clear",
        "Sunny", "Foggy", "Cloudy"
    ]
}

data = pd.DataFrame(data)

# --------------------------------
# 🌍 Function to show weather details & visualization
# --------------------------------
def show_weather(district_name):
    district_data = data[data['District'].str.lower() == district_name.lower()]
    if district_data.empty:
        print("\n❌ District not found in dataset. Try another name.\n")
        return

    row = district_data.iloc[0]
    print(f"\n🌍 Weather Details for {row['District']}:\n")
    time.sleep(0.3)
    print(f"🌡️ Temperature: {row['Temperature(°C)']}°C")
    print(f"💧 Humidity: {row['Humidity(%)']}%")
    print(f"🔵 Pressure: {row['Pressure(hPa)']} hPa")
    print(f"🌀 Wind Speed: {row['WindSpeed(m/s)']} m/s")
    print(f"☁️ Condition: {row['Condition']}")
    print("\n✅ Weather data retrieved successfully!\n")

    print(f"📈 Generating Visual Insights for {district_name}...\n")

    highlight_color = "red"
    normal_color = "skyblue"

    # --------------------------------
    # 1️⃣ Temperature Comparison
    # --------------------------------
    plt.figure(figsize=(10, 5))
    colors = [highlight_color if d.lower() == district_name.lower() else normal_color for d in data['District']]
    sns.barplot(x="District", y="Temperature(°C)", data=data, palette=colors)
    plt.title(f"🌡️ Temperature Comparison ({district_name} highlighted)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=True)

    # --------------------------------
    # 2️⃣ Humidity Line Plot
    # --------------------------------
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="District", y="Humidity(%)", data=data, marker="o", color="green")
    selected = data[data["District"].str.lower() == district_name.lower()]
    plt.scatter(selected["District"], selected["Humidity(%)"], color="red", s=120, label=f"{district_name}")
    plt.title(f"💧 Humidity Trend (highlight: {district_name})")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=True)

    # --------------------------------
    # 3️⃣ Pressure Distribution
    # --------------------------------
    plt.figure(figsize=(6, 5))
    sns.boxplot(y="Pressure(hPa)", data=data, color="lightblue")
    plt.scatter(0, row["Pressure(hPa)"], color="red", s=100, label=f"{district_name}")
    plt.title(f"🔵 Pressure Distribution ({district_name} highlighted)")
    plt.legend()
    plt.tight_layout()
    plt.show(block=True)

    # --------------------------------
    # 4️⃣ Wind Speed Comparison
    # --------------------------------
    plt.figure(figsize=(10, 5))
    plt.bar(data["District"], data["WindSpeed(m/s)"], color="lightgreen")
    plt.bar(row["District"], row["WindSpeed(m/s)"], color="red", label=f"{district_name}")
    plt.title(f"🌀 Wind Speed Comparison ({district_name} highlighted)")
    plt.xlabel("District")
    plt.ylabel("Wind Speed (m/s)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=True)

    # --------------------------------
    # 5️⃣ Weather Condition Distribution
    # --------------------------------
    plt.figure(figsize=(7, 7))
    condition_counts = data["Condition"].value_counts()
    plt.pie(condition_counts, labels=condition_counts.index, autopct="%1.1f%%", startangle=120, shadow=True)
    plt.title("☁️ Weather Condition Distribution Across Districts")
    plt.tight_layout()
    plt.show(block=True)

# --------------------------------
# 🧠 Main program loop
# --------------------------------
while True:
    user_input = input("Enter City/State/District name (or 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        print("\n📂 Analysis completed successfully! Goodbye 👋")
        break
    show_weather(user_input)
