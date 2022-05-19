from typing import List

from pydantic import BaseModel


class DNAMatrixSchema(BaseModel):
    """Base model for the dna matrix."""

    dna: List[str]
