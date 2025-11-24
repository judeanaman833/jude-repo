import pandas as pd        # For data manipulation and CSV reading
import csv                 # For CSV file writing
import math                # For mathematical operations (checking NaN values)
import pathlib             # For path manipulation
import os                  # For file system operations


class WICETL:

    column_year = 2012
    transform = {}
    data = {}
    path = ""
    fields = []
    
    def transform_data(self):
        for i in range(3, 7):
            df = pd.read_csv("C:/Users/Lenovo/Downloads/Openclassroom/JudeOpenclassroomProject/WICAgencies201" + str(i) + "ytd/Infants_Fully_Formula-fed.csv")
            columns = df.columns
            values = df.values.tolist()
            totalQ4 = 0
            totalQ1 = 0
            totalQ2 = 0
            totalQ3 = 0

        for value in values:
            stateQ4 = 0
            stateQ1 = 0
            stateQ2 = 0
            stateQ3 = 0
            state_column_year = self.column_year
            key = ""
            for i in range(0, 15):
                if i == 0:
                    if self.data.get(value[i], None) == None:
                        self.data[value[i]] = {}
                    key = value[i]
                if i > 0 and i <= 3:
                    if math.isnan(value[i]) == False:
                        stateQ4 += value[i]
                        totalQ4 += value[i]
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
            self.data[key]["Q4 " + str(state_column_year)] = stateQ4
            state_column_year += 1
            self.data[key]["Q1 " + str(state_column_year)] = stateQ1
            self.data[key]["Q2 " + str(state_column_year)] = stateQ2
            self.data[key]["Q3 " + str(state_column_year)] = stateQ3
            self.transform["Q4 " + str(self.column_year)] = totalQ4
            self.column_year += 1
            self.transform["Q1 " + str(self.column_year)] = totalQ1
            self.transform["Q2 " + str(self.column_year)] = totalQ2
            self.transform["Q3 " + str(self.column_year)] = totalQ3


    def append_territory(self):
        for state in self.data:
            self.data[state]["State"] = state

        self.path = str(pathlib.Path().resolve())
        self.fields = ["State"] + list(self.transform.keys())


    def write_file(self): 
        if os.path.exists(self.path + "/data") == False:
            os.mkdir(self.path + "/data")


        with open(self.path + "/data/" + "Formula_Fed-Totals.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fields)
            writer.writeheader()

        self.transform["State"] = "All States"
        for state in self.data:
            writer.writerow(self.data[state])

        writer.writerow(self.transform)
        
        wic_etl = WICETL()
        wic_etl.transform_data()
        wic_etl.append_territory()
        wic_etl.write_file()