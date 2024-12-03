import csv
import json

#Load the json data
with open('ce2_defaultOneTime_tn-SnV-2024-12-03T03-42-43_1.json') as config_file:
  data = json.load(config_file)

#Open a CSV file for writing
with open('output.csv', 'w', newline='') as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

  #Write the header (column names)
  writer.writeheader()

  for row in data:
      writer.writerow(row)


