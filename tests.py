import unittest
from api.business import get_medicaments

def test_get_medicaments():
  expectedReturnSucces = {
    "status": 200,
    "response": [
      {
        "DrugName": "Abilify",
        "ActiveIngredient": "Aripiprazole",
        "TypeIngestion": "TABLET;ORAL",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/021436s044s045,021713s035s036,021729s027s028,021866s029s030lbl.pdf#page=77"
      },
      {
        "DrugName": "Abilify",
        "ActiveIngredient": "Aripiprazole",
        "TypeIngestion": "SOLUTION;ORAL",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/021436s044s045,021713s035s036,021729s027s028,021866s029s030lbl.pdf#page=77"
      },
      {
        "DrugName": "Abilify",
        "ActiveIngredient": "Aripiprazole",
        "TypeIngestion": "TABLET, ORALLY DISINTEGRATING;ORAL",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/021436s043,021713s034,021729s026,021866s028lbl.pdf#page=84"
      },
      {
        "DrugName": "Abilify",
        "ActiveIngredient": "Aripiprazole",
        "TypeIngestion": "TABLET, ORALLY DISINTEGRATING;ORAL",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/021436s044s045,021713s035s036,021729s027s028,021866s029s030lbl.pdf#page=77"
      },
      {
        "DrugName": "Abilify",
        "ActiveIngredient": "Aripiprazole",
        "TypeIngestion": "INJECTABLE;INTRAMUSCULAR",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/021436s043,021713s034,021729s026,021866s028lbl.pdf#page=84"
      },
      {
        "DrugName": "Abilify",
        "ActiveIngredient": "Aripiprazole",
        "TypeIngestion": "INJECTABLE;INTRAMUSCULAR",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/021436s044s045,021713s035s036,021729s027s028,021866s029s030lbl.pdf#page=77"
      },
      {
        "DrugName": "Abilify Maintena Kit",
        "ActiveIngredient": "Aripiprazole",
        "TypeIngestion": "FOR SUSPENSION, EXTENDED RELEASE;INTRAMUSCULAR",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/202971s013lbl.pdf#page=52"
      },
      {
        "DrugName": "Abilify Mycite Kit",
        "ActiveIngredient": "Aripiprazole",
        "TypeIngestion": "TABLET;ORAL",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/207202s002s004lbl.pdf#page=48"
      },
      {
        "DrugName": "Abilify Mycite Kit",
        "ActiveIngredient": "Aripiprazole",
        "TypeIngestion": "TABLET;ORAL",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/207202s003lbl.pdf#page=44"
      },
      {
        "DrugName": "Aristada",
        "ActiveIngredient": "Aripiprazole LAuroxil",
        "TypeIngestion": "SUSPENSION, EXTENDED RELEASE;INTRAMUSCULAR",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/207533s004lbl.pdf#page=35"
      },
      {
        "DrugName": "Aristada",
        "ActiveIngredient": "Aripiprazole LAuroxil",
        "TypeIngestion": "SUSPENSION, EXTENDED RELEASE;INTRAMUSCULAR",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/207533s017,209830s005lbl.pdf#page=36"
      },
      {
        "DrugName": "Aristada Initio Kit",
        "ActiveIngredient": "Aripiprazole LAuroxil",
        "TypeIngestion": "SUSPENSION, EXTENDED RELEASE;INTRAMUSCULAR",
        "Link": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/207533s017,209830s005lbl.pdf#page=72"
      }
    ]
  }    
  expectedReturnNotFound = {
  "status": 210,
  "error": "Not found medicaments whit Active Ingredient 'test'"
  }
  
  expectedReturnfail = {
  "status": 500,
  "response": "Ops. We gotta a problem"
  }

  assert (get_medicaments('Aripiprazole') == expectedReturnSucces)
  assert (get_medicaments('test') == expectedReturnNotFound)
  assert (get_medicaments('[') == expectedReturnfail)


test_get_medicaments()
print("Everything passed")