from typing import List

from pydantic import BaseModel


class PersonSchema(BaseModel):
    dna: List
    is_mutant: bool
