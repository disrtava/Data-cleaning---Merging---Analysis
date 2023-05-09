import csv

data=[]

with open('final.csv') as f:
  reader=csv.reader(f)
  for row in reader:
    data.append(row)

headers=data[0]
star_data_rows=data[1:]

star_gravity = []

for i in star_data_rows:

  gravity = ((6.67*(10**-11)) * i[3]*1.989e+30)/(i[7] * 6.957e+8)**2
  star_gravity.append(gravity)