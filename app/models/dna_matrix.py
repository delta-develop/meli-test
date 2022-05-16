from dataclasses import Field
from pydantic import BaseModel
from typing import List


class DNAMatrixSchema(BaseModel):
    dna: List[str]
