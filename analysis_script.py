import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv('rides.csv')

# Step 2: Show the first few records
print("🛺 First few rides:")
print(df.head())

# Step 3: Total number of rides
total_rides = len(df)
print("\n🔢 Total Rides:", total_rides)

# Step 4: Total earnings from all rides
total_earnings = df['price'].sum()
print("💰 Total Earnings: ₹", total_earnings)

# Step 5: Most common source location
top_source = df['source'].mode()[0]
print("📍 Most Common Source Location:", top_source)

# Step 6: Earnings by each driver
driver_earnings = df.groupby('driver_id')['price'].sum()
print("\n🧑‍✈️ Earnings by Driver:")
print(driver_earnings)

# Step 7: Plot - Driver-wise Earnings (Bar Chart)
driver_earnings.plot(kind='bar', color='skyblue')
plt.title('Driver-wise Earnings')
plt.xlabel('Driver ID')
plt.ylabel('Earnings (₹)')
plt.grid(True)
plt.tight_layout()
plt.savefig('static/driver_earnings.png')  # save to static folder
plt.show()

# Step 8: Plot - Ride Count from Each Source (Pie Chart)
source_counts = df['source'].value_counts()
source_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Rides from Each Source')
plt.ylabel('')
plt.savefig('static/source_distribution.png')  # save to static folder
plt.show()
