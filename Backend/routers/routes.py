'''Endpoint creation'''
from fastapi import APIRouter, Depends, HTTPException
from schemas.schemas import TeamInput
from utils.api_client import NBA_Client

nba_router = APIRouter(tags = ["NBA"])
nba_api = NBA_Client()


@nba_router.post('/team')
async def get_team_by_search(user_input: TeamInput):
    team_param = user_input.search_param
    team_id = nba_api.get_team_id(team_param=team_param)
    return team_id