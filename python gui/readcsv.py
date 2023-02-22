# import csv 

# def readcsv():
#     with open('data.csv',newline='',encoding='utf-8') as file:
#         fr  = list(csv.reader(file))
#         print(fr)
        
#         readcsv()

import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Call the function to read the CSV file
file_path = 'data.csv'
data = read_csv(file_path)

# Print the data
for row in data:
    # print(row)

    read_csv(file_path)



# import csv

# # Open the CSV file
# def readcsv():
#     with open('data.csv', 'r',newline='',encoding='utf-8') as file:
#     # Create a CSV reader object
#         reader = list(csv.reader(file))
#         print(reader)

#         readcsv()
