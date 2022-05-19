from typing import List

from pydantic import BaseModel


class DNAMatrixSchema(BaseModel):
    dna: List[str]
