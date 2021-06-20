from typing import Optional
from fastapi import FastAPI
import sys

app = FastAPI()


@app.get("/{active_ingredient}")
def read_item(active_ingredient: Optional[str] = None):

  import csv
  meds = []
  try:
    with open('./app/MedicationGuides.csv') as file:
      fileReader = csv.reader(file, delimiter=',')
      for row in fileReader:
        if active_ingredient in row[1]:
          meds.append({
            "Drug Name": row[0],
            "Active Ingredient": row[1],
            "Type/Ingestion": row[2],
            "Link": row[-1]
          })
    if len(meds)<1:
      meds.append({
        "error" : f"no medicine was found that contains '{active_ingredient}'"
      })
    return meds

  except:
    return {"error":"something get wrong "}


      