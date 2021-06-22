from fastapi import APIRouter
from api.business import get_medicaments

router = APIRouter()


@router.get("/app/{active_ingredient}")
async def find_medicaments(active_ingredient):
  return get_medicaments(active_ingredient)

