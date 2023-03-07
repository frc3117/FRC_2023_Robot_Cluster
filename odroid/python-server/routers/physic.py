from requestutils import response
from fastapi import APIRouter

router = APIRouter(prefix='/simulation')

@router.post("/start")
async def start_simulation():
    pass

@router.get("/list")
async def simulation_list():
    return response(data=[1, 2, 3])

@router.get("/status/{sim_uuid}")
async def simulation_status(sim_uuid: str):
    pass

@router.get('/results/{sim_uuid}')
async def simulation_results(sim_uuid: str):
    pass

@router.get('/results-peek/{sim_uuid}')
async def simulation_results_peek(sim_uuid: str):
    pass