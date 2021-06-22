from api.model import Medicament
from typing import Optional


def get_medicaments(active_ingredient: Optional[str] = None):
  import csv
  import pandas as pd
  try:
    meds = []
    medicationGuides = pd.read_csv("./api/MedicationGuides.csv")
    numpyMed = medicationGuides.loc[medicationGuides.ActiveIngredient.str.contains(active_ingredient)].to_numpy()
    for item in range(len(numpyMed)):
      med = Medicament(
        DrugName=numpyMed[item][0],
        ActiveIngredient=numpyMed[item][1],
        TypeIngestion=numpyMed[item][2],
        Link=numpyMed[item][-1]
        )
      meds.append(med)

    if len(meds)<1:
      raise ValueError
    
    else:
      response = {
        "status": 200,
        "response": meds
      }
      return response

  except ValueError:
    response = {
      "status": 210,
      "error": f"Not found medicaments whit Active Ingredient '{active_ingredient}'"
    }
    return response

  except:
    response = {
      "status": 500,
      "response": "Ops. We gotta a problem"
    }
    return response