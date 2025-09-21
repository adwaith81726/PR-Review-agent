from pydantic import BaseModel
from typing import List

class PRResponse(BaseModel):
    feedback: str
    issues: List[str]
