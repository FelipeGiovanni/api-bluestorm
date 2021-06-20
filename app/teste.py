import csv

def read_item(active_ingredient):
  import csv
  meds = []
  with open('MedicationGuides.csv') as file:
    fileReader = csv.reader(file, delimiter=',')
    for row in fileReader:
      if active_ingredient in row[1]:
        meds.append(row)
        """
        print ({
          "Drug Name": row[0],
          "Active Ingredient": row[1],
          "Form": row[2],
          "Link": row[-1]
        })
        """
    for i in meds:
      print({
          "Drug Name": i[0],
          "Active Ingredient": i[1],
          "Form": i[2],
          "Link": i[-1]
        })

#read_item('Olanz')

a = []
print(len(a))
