from dataclasses import Field
from pydantic import BaseModel
from typing import List


class PersonSchema(BaseModel):
    dna: List
    is_mutant: bool
