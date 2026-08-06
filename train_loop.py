# A Python list containing your actual Western Line commute stations 
western_line_stations = [
     "Virar" , "Nalla Sopara" , "Vasai Road" , "Naigoan" , "Bhayandar" , "Mira Road" , "Dahisar" , "Borival" , "Andheri" , "Bandra" ]

 # The 'for' loop reads each station name one by one automatically 
for station in western_line_stations:
      print(f"The train has arrived at: {station}")

# This line runs ONLY after the loop finishes visiting every station in the list
print("\nArrived at Bandra! Time to head to Fr. CRCE and build the empire.")