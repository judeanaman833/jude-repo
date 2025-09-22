import pandas as pd        # For data manipulation and CSV reading
import csv                 # For CSV file writing
import math                # For mathematical operations (checking NaN values)
import pathlib             # For path manipulation
import os                  # For file system operations


column_year = 2012         # Starting year for data processing
transform = {}             # Dictionary to store national totals
data = {}                  # Dictionary to store state-level data


for i in range(3, 7):      # Loops through years 2013-2016
  df = pd.read_csv("C:/Users/Lenovo/Downloads/Openclassroom/JudeOpenclassroomProject/WICAgencies201" + str(i) + "ytd/Infants_Fully_Formula-fed.csv")
  columns = df.columns
  values = df.values.tolist()   # Convert DataFrame to list of lists
  totalQ4 = 0
  totalQ1 = 0
  totalQ2 = 0
  totalQ3 = 0
  
  for value in values:
    stateQ4 = 0  # State-specific Q4 total
    stateQ1 = 0  # State-specific Q1 total
    stateQ2 = 0  # State-specific Q2 total
    stateQ3 = 0  # State-specific Q3 total

    state_column_year = column_year
    key = ""
    for i in range(0, 15):
      if i == 0:  # State name column
        if data.get(value[i], None) == None:
          data[value[i]] = {}  # Initialize state entry
        key = value[i]   # Store state name as key        
         # Process quarterly data, checking for NaN values
      if i > 0 and i <= 3:  # Q4 columns
        if math.isnan(value[i]) == False:
          stateQ4 += value[i]
          totalQ4 += value[i]
            # Similar logic for other quarters...
      if i > 3 and i <= 6:
        if math.isnan(value[i]) == False:
          stateQ1 += value[i]
          totalQ1 += value[i]
      if i > 6 and i <= 9:
        if math.isnan(value[i]) == False:
          stateQ2 += value[i]
          totalQ2 += value[i]
      if i > 9 and i <= 12:
        if math.isnan(value[i]) == False:
          stateQ3 += value[i]
          totalQ3 += value[i]
    data[key]["Q4 " + str(state_column_year)] = stateQ4
    state_column_year+=1
    data[key]["Q1 " + str(state_column_year)] = stateQ1
    data[key]["Q2 " + str(state_column_year)] = stateQ2
    data[key]["Q3 " + str(state_column_year)] = stateQ3
  transform["Q4 " + str(column_year)] = totalQ4
  column_year+=1
  transform["Q1 " + str(column_year)] = totalQ1
  transform["Q2 " + str(column_year)] = totalQ2
  transform["Q3 " + str(column_year)] = totalQ3

for state in data:
  data[state]["State"] = state  # Add state name to each state's data

path = str(pathlib.Path().resolve())  # Get current directory
fields = ["State"] + list(transform.keys())  # Column headers

if os.path.exists(path + "/data") == False:
    os.mkdir(path + "/data")  # Create output directory if it doesn't exist

# Write to CSV file
with open(path + "/data/" + "Formula_Fed-Totals.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    transform["State"] = "All States"  # Label for national totals
    for state in data:
        writer.writerow(data[state])  # Write state data
    writer.writerow(transform)  # Write national totals
