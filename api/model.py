from pydantic import BaseModel


class Medicament(BaseModel):
    DrugName: str
    ActiveIngredient: str
    TypeIngestion: str
    Link: str
