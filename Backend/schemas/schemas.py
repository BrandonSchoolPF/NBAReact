from pydantic import BaseModel
from typing import Optional

class TeamInput(BaseModel):
    search_param : str