# 1. Defining the automated processing machine
def calculate_channel_payout(views, rpm_rate):
    """Calculates dollar earnings based on views and RPM."""
    return (views / 1000) * rpm_rate

# 2. Setting up raw data in a single Python Dictionary
# Structure: "Country": {"views": amount, "rpm": rate}
channel_data = {
    "US": {"views": 250000, "rpm": 8.50},
    "UK": {"views": 120000, "rpm": 6.20},
    "Canada": {"views": 85000, "rpm": 5.40}  # Easily add more data!
}

total_combined_value = 0

print("--- HIGH-RPM CHANNEL REVENUE REPORT ---")

# 3. Running the inputs through the 'for' loop automatically
for country, stats in channel_data.items():
    # Extracting values from the sub-dictionary
    views = stats["views"]
    rpm = stats["rpm"]
    
    # Calculation
    income = calculate_channel_payout(views, rpm)
    total_combined_value += income
    
    # 4. Printing formatted results
    print(f"Projected {country} Earnings: ${income:.2f} from {views:,} views at ${rpm}/1k views")

print(f"Total Combined Pipeline Value: ${total_combined_value:.2f}")