import csv

data=[]

with open('final.csv') as f:
  reader=csv.reader(f)
  for row in reader:
    data.append(row)

headers=data[0]
star_data_rows=data[1:]

