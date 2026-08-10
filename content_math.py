# 1. Defining the automated processing machine
def calculate_channel_payout(views, rpm_rate):
  """
  This function takes total views and the country-specific RPM rate, calculates the dollar earnings, and returns the final amount.
  """
  dollar_earnings = (views / 1000) * rpm_rate
  return dollar_earnings

# 2. Setting up raw data inputs for different global audiences 

us_views = 250000
us_rpm = 8.50  # US advertisers pay high rates ($8.50 per 1k views)

uk_views = 120000
uk_rpm = 6.20  # UK advertisers pay mid-tier rates ($6.20 per 1k views)

# 3. Running the inputs through the function machine
us_income = calculate_channel_payout(us_views, us_rpm)
uk_income = calculate_channel_payout(uk_views, uk_rpm)

# 4. Printing the formatted results to the terminal console
print("--- HIGH-RPM CHANNEL REVENUE REPORT ---")
print(f"Projected US Earnings: ${us_income:.2f} from {us_views} views at ${us_rpm}/1k views")
print(f"Projected UK Earnings: ${uk_income:.2f} from {uk_views} views at ${uk_rpm}/1k views")
print(f"Total Combined Pipeline Value: ${us_income + uk_income:.2f}")