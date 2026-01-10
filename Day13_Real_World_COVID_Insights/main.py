import pandas as pd
import matplotlib.pyplot as plt

# Load CSV dataset
df = pd.read_csv("C:\\Users\Manisha\OneDrive\Documents\covid_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

print("\nDATASET OVERVIEW")
print("Total Countries:", df['Country/Region'].nunique())
print("Total Confirmed Cases:", int(df['Confirmed'].sum()))
print("Total Deaths:", int(df['Deaths'].sum()))
print("Total Recovered:", int(df['Recovered'].sum()))

# 🔥 Top 10 affected countries
top_countries = df.sort_values(by='Confirmed', ascending=False).head(10)

print("\nTOP 10 MOST AFFECTED COUNTRIES")
print(top_countries[['Country/Region', 'Confirmed', 'Deaths', 'Recovered']])

# 📊 Bar Chart – Top 10 Countries
plt.figure(figsize=(10,5))
plt.bar(top_countries['Country/Region'], top_countries['Confirmed'])
plt.xticks(rotation=45)
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.tight_layout()
plt.show()

# 📍 Country-wise Insight
country = "India"
country_data = df[df['Country/Region'] == country]

print(f"\nINSIGHTS FOR {country.upper()}")
print("Confirmed:", int(country_data['Confirmed']))
print("Deaths:", int(country_data['Deaths']))
print("Recovered:", int(country_data['Recovered']))
print("Active Cases:", int(country_data['Active']))

# 📈 Pie Chart – Case Distribution
labels = ['Active', 'Recovered', 'Deaths']
values = [
    int(country_data['Active']),
    int(country_data['Recovered']),
    int(country_data['Deaths'])
]

plt.figure(figsize=(6,6))
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title(f"COVID-19 Case Distribution in {country}")
plt.show()